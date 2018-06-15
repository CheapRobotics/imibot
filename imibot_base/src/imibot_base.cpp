#include "ros/ros.h"
#include "imibot_hardware.h"
#include "controller_manager/controller_manager.h"


int main(int argc, char *argv[])
{
	ros::init(argc, argv, "imibot_base");

	imibot_base::ImibotHardware robot;
	controller_manager::ControllerManager cm(&robot);

	ros::AsyncSpinner spinner(1);
    spinner.start();

    ros::Time prev_time = ros::Time::now();
    ros::Rate rate(10.0);

    while(ros::ok())
    {

    	const ros::Time time = ros::Time::now();
    	const ros::Duration period = time - prev_time;

    	robot.updateJointsFromHardware();
    	cm.update(time, period);
    	robot.writeCommandsToHardware();

    	rate.sleep();
    }
    return 0;
	
}