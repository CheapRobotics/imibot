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
        ImibotHardware();

        void updateJointsFromHardware(); // read()

        void writeCommandsToHardware();  // write()

    private:

        void registerControlInterfaces();

        double linearToAngular(const double &travel) const;

        double angularToLinear(const double &angle) const;

        void limitDifferentialSpeed(double &travel_speed_left, double &travel_speed_right);

        ros::NodeHandle nh_;

        hardware_interface::JointStateInterface joint_state_interface_;
        hardware_interface::VelocityJointInterface velocity_joint_interface_;

        double wheel_diameter_, max_accel_, max_speed_;

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
