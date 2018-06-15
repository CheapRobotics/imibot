#include "imibot_hardware.h"

namespace
{
	const uint8_t LEFT = 0, RIGHT = 1;
}

namespace imibot_base
{

  ImibotHardware::ImibotHardware()
  {

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