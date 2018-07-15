#include "imibot_hardware.h"
#include "ros/ros.h"
#include "imibot_driver/StickControl.h"
#include <boost/assign/list_of.hpp>
#include <string>
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
    this->cmd_pub = nh_.advertise<imibot_driver::StickControl>("robot_mg", 1000, false);
    registerControlInterfaces();
  }

  void ImibotHardware::registerControlInterfaces()
  {
    ros::V_string joint_names = boost::assign::list_of("front_left_wheel")
      ("front_right_wheel")("rear_left_wheel")("rear_right_wheel");
    for (unsigned int i = 0; i < joint_names.size(); i++)
    {
      hardware_interface::JointStateHandle joint_state_handle(joint_names[i],
                                                              &joints_[i].position, &joints_[i].velocity,
                                                              &joints_[i].effort);
      joint_state_interface_.registerHandle(joint_state_handle);

      hardware_interface::JointHandle joint_handle(
        joint_state_handle, &joints_[i].velocity_command);
      velocity_joint_interface_.registerHandle(joint_handle);
    }
    registerInterface(&joint_state_interface_);
    registerInterface(&velocity_joint_interface_);
  }

  void ImibotHardware::updateJointsFromHardware()
  {


  }

  void ImibotHardware::writeCommandsToHardware()
  {
    double diff_speed_left = angularToLinear(joints_[LEFT].velocity_command);
    double diff_speed_right = angularToLinear(joints_[RIGHT].velocity_command);

    cout << "left  : " << diff_speed_left << endl;
    cout << "right : " << diff_speed_right << endl;

    imibot_driver::StickControl msg;
    msg.strength = diff_speed_left; // Read from velocity_joint_interface_ 
    msg.angle = diff_speed_right;     // Read from velocity_joint_interface_

    this->cmd_pub.publish(msg);
  }

  double ImibotHardware::linearToAngular(const double &travel) const
  {
  	return travel / wheel_diameter_ * 2;
  }

  double ImibotHardware::angularToLinear(const double &angle) const
  {
  	return angle * wheel_diameter_ / 2;
  }

  void ImibotHardware::limitDifferentialSpeed(double &travel_speed_left, double &travel_speed_right)
  {
    /*
    double large_speed = std::max(std::abs(diff_speed_left), std::abs(diff_speed_right));

    if (large_speed > max_speed_)
    {
      diff_speed_left *= max_speed_ / large_speed;
      diff_speed_right *= max_speed_ / large_speed;
    }
    */
  }


}