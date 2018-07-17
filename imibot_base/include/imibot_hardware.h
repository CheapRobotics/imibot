#ifndef IMIBOT_HARDWARE_H
#define IMIBOT_HARDWARE_H

#include "hardware_interface/joint_state_interface.h"
#include "hardware_interface/joint_command_interface.h"
#include "hardware_interface/robot_hw.h"
#include "ros/ros.h"
#include "sensor_msgs/JointState.h"
#include <string>

namespace imibot_base
{

  class ImibotHardware:
    public hardware_interface::RobotHW
  {

    public:
    	ImibotHardware(ros::NodeHandle nh);

    	void updateJointsFromHardware(); // read()

    	void writeCommandsToHardware();  // write()

    private:

        void registerControlInterfaces();

        void getLastSensorsValues(const std_msgs::String &msg);

        double linearToAngular(const double &travel) const;

        double angularToLinear(const double &angle) const;

    	void limitDifferentialSpeed(double &travel_speed_left, double &travel_speed_right);

    	ros::NodeHandle nh_;
        ros::Publisher cmd_pub;
        ros::Subscriber speed_sensors_sub_;

    	hardware_interface::JointStateInterface joint_state_interface_;
    	hardware_interface::VelocityJointInterface velocity_joint_interface_;

    	double wheel_diameter_, max_accel_, max_speed_, left_speed, right_speed, left_travel, right_travel;

    	struct Joint
    	{
    		double position;
    		double position_offset;
    		double velocity;
    		double effort;
    		double velocity_command;

    		Joint() :
    		  position(0), velocity(0), effort(0), velocity_command(0)
    		  { }
    	} joints_[4];

  };
}

#endif // IMIBOT_HARDWARE_H