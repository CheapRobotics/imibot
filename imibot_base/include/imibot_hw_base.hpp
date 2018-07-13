#ifndef IMIBOT_HW_BASE_H
#define IMIBOT_HW_BASE_H

#define GPIO_22 6
#define GPIO_23 13
#define GPIO_24 19
#define GPIO_25 26

namespace imibot_base
{

  class ImibotHWBase
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
    private:
      gpio gpio22(GPIO_22);
      gpio gpio23(GPIO_23);
      gpio gpio24(GPIO_24);
      gpio gpio25(GPIO_25);

 };

}
#endif // IMIBOT_HW_BASE_H
