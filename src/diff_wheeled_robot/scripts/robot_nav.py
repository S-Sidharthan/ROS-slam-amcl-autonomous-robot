#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

from tf.transformations import euler_from_quaternion


front = 0.0
left = 0.0
right = 0.0

roll = pitch = yaw = 0.0

def laser_callback(msg):
	global front,right,left
	right = min(min(msg.ranges[0:143]),10)		#0-36degrees
	front = min(min(msg.ranges[288:432]),10)  	#72-108 deg
	left = min(min(msg.ranges[577:719]),10)		#144-180 deg

def odom_callback(msg):
	global roll, pitch, yaw
	o = msg.pose.pose.orientation
	o_q = [o.x,o.y,o.z,o.w]

	(roll,pitch,yaw) = euler_from_quaternion(o_q)




rospy.init_node('bot_contoller')
msg = Twist()
msg.linear.x = 0.0
msg.angular.z = 0.0
pub = rospy.Publisher('/cmd_vel',Twist, queue_size = 10)
rospy.Subscriber('/scan',LaserScan,laser_callback)
rospy.Subscriber('/odom',Odometry,odom_callback)

rate = rospy.Rate(10)

while not rospy.is_shutdown():
	if(front>0.5):
		msg.linear.x = 0.5
		msg.angular.z = 0

	else:
		msg.linear.x =0
		if(right > left):
			msg.angular.z = -0.25
		else:
			msg.angular.z = 0.25	


	if(front>0.5):
		msg.linear.x = 0.25

	elif(front< 0.5):
		if(right > left):
			msg.angular.z = -0.25
		else:
			msg.angular.z = 0.25


	if(right < 0.5):
		msg.angular.z = 0.5 - right
	if(left < 0.5):
		msg.angular.z = left - 0.5

	msg.linear.z = 0.1

	pub.publish(msg)


	