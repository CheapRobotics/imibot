#ifndef IMIBOT_HW_BASE_H
#define IMIBOT_HW_BASE_H

namespace imibot_base
{

  class ImibotHWBase:
  {
    public:
      ImibotHWBase();
      void stop();
      void forward();
      void reverse();
      void turnLeft();
      void turnRight();
      void setLeftSpeed();
      void setRightSpeed();
      void setTotalSpeed();
 }

}
#endif // IMIBOT_HW_BASE_H
