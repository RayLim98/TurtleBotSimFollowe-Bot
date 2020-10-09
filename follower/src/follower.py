#!/usr/bin/env python
import rospy
import cv2
import numpy as np
import argparse
import imutils
import time
from ball_yellow import tracker
from collections import deque
#from imutils.video import VideoStreampip 
from cv_bridge          import CvBridge, CvBridgeError

from sensor_msgs.msg    import Image
from geometry_msgs.msg  import Twist

class Follow:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/tb3_0/camera/rgb/image_raw",Image,self.callback)
    self.velocity_publisher = rospy.Publisher('/tb3_0/cmd_vel', Twist, queue_size=10)
    self.vel_msg = Twist()
  # def setXY(self,x):
  #   self.__x = x

  # def getXY(self):
  #   return self.__x
    
  def callback(self,data):
    angular_velocity = 0
    linear_velocity = 0
    cv_image = self.bridge.imgmsg_to_cv2(data) # converts ROS image to OpenCV image 
    cv2.imshow("Image window",cv_image) #Uncomment this if you want to see a live feed
    cv2.waitKey(1)                      #from simulation (makes sure you have open CV)

    ####################################################################
    # image procesing logic goes here
    information = tracker(cv_image)
    linear_velocity = information[0]
    angular_velocity = information[1]
    ####################################################################
    self.vel_msg.angular.z = angular_velocity
    self.vel_msg.linear.x =  linear_velocity 
    self.velocity_publisher.publish(self.vel_msg)


def main():
  rospy.init_node('image_topic', anonymous=True)
  ic = Follow()

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting Down")
    cv2.destroyAllWindows()
  

if __name__ == "__main__":
  main()
