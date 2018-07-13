#include "imibot_hardware.h"
#include <boost/assign/list_of.hpp>

namespace
{
	const uint8_t LEFT = 0, RIGHT = 1;
}

namespace imibot_base
{

  ImibotHardware::ImibotHardware()
  {
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

  }

  double ImibotHardware::linearToAngular(const double &travel) const
  {
  	return 0;
  }

  double ImibotHardware::angularToLinear(const double &angle) const
  {
  	return 0;
  }

  void ImibotHardware::limitDifferentialSpeed(double &travel_speed_left, double &travel_speed_right)
  {

  }


}