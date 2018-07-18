#include "imibot_hardware.h"
#include "ros/ros.h"
#include "imibot_driver/DiffSpeed.h"
#include "imibot_driver/SensorsReadings.h"
#include <boost/assign/list_of.hpp>
#include <iostream>

namespace
{
	const uint8_t LEFT = 0, RIGHT = 1;
}

using namespace std;

namespace imibot_base
{

  ImibotHardware::ImibotHardware(ros::NodeHandle nh)
  :
  nh_(nh)
  {
    nh_.param<double>("wheel_diameter", wheel_diameter_, 0.066);
    nh_.param<double>("max_accel", max_accel_, 5.0);
    nh_.param<double>("max_speed", max_speed_, 1.0);
    this->cmd_pub = nh_.advertise<imibot_driver::DiffSpeed>("robot_mg", 1000, false);
    registerControlInterfaces();
    ros::Subscriber speed_sensors_sub_ = nh_.subscribe("imibot/speed_sensors", 1, &ImibotHardware::getLastSensorsValues, this);
  }

  void ImibotHardware::registerControlInterfaces()
  {
    ros::V_string joint_names = boost::assign::list_of("front_left_wheel")("front_right_wheel")("rear_left_wheel")("rear_right_wheel");

    for (unsigned int i = 0; i < joint_names.size(); i++)
    {
      hardware_interface::JointStateHandle joint_state_handle(joint_names[i],
                                                              &joints_[i].position, &joints_[i].velocity,
                                                              &joints_[i].effort);
      joint_state_interface_.registerHandle(joint_state_handle);

      hardware_interface::JointHandle joint_handle(joint_state_handle, &joints_[i].velocity_command);
      velocity_joint_interface_.registerHandle(joint_handle);
    }
    registerInterface(&joint_state_interface_);
    registerInterface(&velocity_joint_interface_);
  }

  void ImibotHardware::getLastSensorsValues(const imibot_driver::SensorsReadings::ConstPtr& msg)
  {
    left_speed = msg->left_measured_vel;
    right_speed = msg->right_measured_vel;
    left_travel = msg->left_measured_travel;
    right_travel = msg->right_measured_travel;
  }

  void ImibotHardware::updateJointsFromHardware()
  {
    for (int i = 0; i < 2; i++)
    {
      double delta_left = linearToAngular(left_travel) - joints_[i].position;

      joints_[i].position += delta_left;
      joints_[i].velocity = linearToAngular(left_travel);
    }
    for (int i = 2; i < 4; i++)
    {
      double delta_right = linearToAngular(right_travel) - joints_[i].position;

      joints_[i].position += delta_right;
      joints_[i].velocity = linearToAngular(right_travel);
    }
  }


  /**
  * Get latest velocity commands from ros_control via joint structure, and send to MCU
  */
  void ImibotHardware::writeCommandsToHardware()
  {
    double diff_speed_left = angularToLinear(joints_[LEFT].velocity_command);
    double diff_speed_right = angularToLinear(joints_[RIGHT].velocity_command);

    limitDifferentialSpeed(diff_speed_left, diff_speed_right);

    cout << "left  : " << diff_speed_left << endl;
    cout << "right : " << diff_speed_right << endl;

    imibot_driver::DiffSpeed msg;
    msg.left_speed = diff_speed_left * 100; // Read from velocity_joint_interface_ 
    msg.right_speed = diff_speed_right * 100;     // Read from velocity_joint_interface_

    this->cmd_pub.publish(msg);
  }


  /**
  * Scale left and right speed outputs to maintain ros_control's desired trajectory without saturating the outputs
  */
  void ImibotHardware::limitDifferentialSpeed(double &diff_speed_left, double &diff_speed_right)
  {
    double large_speed = std::max(std::abs(diff_speed_left), std::abs(diff_speed_right));

    if (large_speed > max_speed_)
    {
      diff_speed_left *= max_speed_ / large_speed;
      diff_speed_right *= max_speed_ / large_speed;
    }
  }

  /**
  * Husky reports travel in metres, need radians for ros_control RobotHW
  */
  double ImibotHardware::linearToAngular(const double &travel) const
  {
    return travel / wheel_diameter_ * 2;
  }

  /**
  * RobotHW provides velocity command in rad/s, Husky needs m/s,
  */
  double ImibotHardware::angularToLinear(const double &angle) const
  {
    return angle * wheel_diameter_ / 2;
}


}