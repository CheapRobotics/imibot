#include "imibot_hw_base.hpp"
#include "gpio.h"

#define GPIO_22 6
#define GPIO_23 13
#define GPIO_24 19
#define GPIO_25 26


namespace imibot_base
{

  ImibotHWBase::ImibotHWBase()
  {
/*    wiringPiSetup () ;
    pinMode (GPIO_22, OUTPUT) ;
    pinMode (GPIO_23, OUTPUT) ;
    pinMode (GPIO_24, OUTPUT) ;
    pinMode (GPIO_25, OUTPUT) ;*/
//    GPIO.setup(26, GPIO.OUT)
//    GPIO.setup(19, GPIO.OUT)
//    GPIO.setup(13, GPIO.OUT)
//    GPIO.setup(6, GPIO.OUT)
//    GPIO.output(26, False)
//    GPIO.output(13, False)
//    GPIO.output(19, False)
//    GPIO.output(6, False)
    this->stop();
  }

  /**
   *
   * GPIO.output(26, False)
   * GPIO.output(13, False)
   * GPIO.output(19, False)
   * GPIO.output(6, False)
   */
  void ImibotHWBase::stop()
  {
    this->gpio22=0;
    this->gpio23=0;
    this->gpio24=0;
    this->gpio25=0;
/*
    digitalWrite (GPIO_22,  LOW);
    digitalWrite (GPIO_23,  LOW);
    digitalWrite (GPIO_24,  LOW);
    digitalWrite (GPIO_25,  LOW);
*/
  }

  /**
   * GPIO.output(26, False)
   * GPIO.output(13, False)
   * GPIO.output(19, True)
   * GPIO.output(6, True)
   */
  void ImibotHWBase::forward()
  {
    this->gpio22=1;
    this->gpio23=0;
    this->gpio24=2;
    this->gpio25=0;
/*
    digitalWrite (GPIO_22,  HIGH);
    digitalWrite (GPIO_23,  LOW);
    digitalWrite (GPIO_24,  HIGH);
    digitalWrite (GPIO_25,  LOW);
*/
  }

  /**
   * GPIO.output(19, False)
   * GPIO.output(6, False)
   * GPIO.output(26, True)
   * GPIO.output(13, True)
   */
  void ImibotHWBase::reverse()
  {
/*
    digitalWrite (GPIO_22,  LOW);
    digitalWrite (GPIO_23,  HIGH);
    digitalWrite (GPIO_24,  LOW);
    digitalWrite (GPIO_25,  HIGH);
*/
  }

  /**
   * GPIO.output(26, False)
   * GPIO.output(6, False)
   * GPIO.output(13, True)
   * GPIO.output(19, True)
   */
  void ImibotHWBase::turnLeft()
  {
/*
    digitalWrite (GPIO_22,  LOW);
    digitalWrite (GPIO_23,  HIGH);
    digitalWrite (GPIO_24,  HIGH);
    digitalWrite (GPIO_25,  LOW);
*/
  }

  /**
   * GPIO.output(13, False)
   * GPIO.output(6, True)
   * GPIO.output(19, False)
   * GPIO.output(26, True)
   */
  void ImibotHWBase::turnRight()
  {
    digitalWrite (GPIO_22,  HIGH);
    digitalWrite (GPIO_23,  LOW);
    digitalWrite (GPIO_24,  LOW);
    digitalWrite (GPIO_25,  HIGH);
  }

  void ImibotHWBase::setLeftSpeed()
  {

  }

  void ImibotHWBase::setRightSpeed()
  {

  }

  void ImibotHWBase::setTotalSpeed()
  {

  }

}
