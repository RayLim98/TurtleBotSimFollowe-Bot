# TurtleBotSimFollowe-Bot

## Code:
The code utilizes the following resources: OpenCV, Ros, Python, and Catkin Workspace. Using catkin workspace, we made a package called ‘follower’. Follower has two python scripts called follower, which is the main script that communicates with ROS, and greenball_detection, which is an imaging processing algorithm that uses OpenCV. Using these resources, we were able to make a robot follow any object that is a green circle. We equipped a guider robot with a green sphere to meet this need.


The scripts are broken down into two distinct roles to reinforce modularity:

### Follower.py
This is the main script. It creates a node that communicates to the ros network by importing rospy, allowing us to access rospy methods for subscribing and publishing. Our node subscribes to the rgb camera of our robot and publishes movement topic (cmd_vel) commands back to the robot. This is the crux of our algorithm.
Follower has a class called Follow. Follow has a callback function that runs when subscriber data comes. Data, which is in type Image, is passed in as an argument in the function called tracker. Tracker then returns the required linear, angular velocity and publishes those values back to the robot.

### Greenball_detection.py

This script is imported into the main script. Its main function is called tracker, which takes in an argument and uses open CV with NumPy to compute the argument data. It locates the centroid of a ball on the x and y plane of the image, allowing us to compute the angular velocity. OpenCV also allows us to detect the radius of the ball. This allows us to gauge the distance and start and stop at a certain distance allowing us to compute the linear velocity. We then return linear and angular velocity as an array back to the function. This function is called in the main script, follower, which is then published to the robot.
