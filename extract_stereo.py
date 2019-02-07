#!/usr/bin/env python

import cv2
import sys
import numpy as np
import sys, time

# numpy and scipy
import numpy as np
from scipy.ndimage import filters

# OpenCV
import cv2

# Ros libraries
import roslib
import rospy

# Ros Messages
from sensor_msgs.msg import CompressedImage

def main():
	cap = cv2.VideoCapture(int(sys.argv[1]))
	cap.set(cv2.CAP_PROP_CONVERT_RGB, False)
	image_pub_left = rospy.Publisher("/camera/left/image_raw",CompressedImage,queue_size=10)
	image_pub_right = rospy.Publisher("/camera/right/image_raw",CompressedImage,queue_size=10)
	rospy.init_node('image_feature', anonymous=True)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		ret,frame = cap.read()

		left = frame[:,:,0]
		right = frame[:,:,1]
		#### Create CompressedIamge ####
		msg_left = CompressedImage()
		msg_right = CompressedImage()
		msg_left.header.stamp = rospy.Time.now()
		msg_right.header.stamp = rospy.Time.now()
		msg_left.format = "jpeg"
		msg_right.format = "jpeg"
		msg_left.data = np.array(cv2.imencode('.jpg', left)[1]).tostring()
		msg_right.data = np.array(cv2.imencode('.jpg', right)[1]).tostring()
		# Publish new image
		image_pub_left.publish(msg_left)
		image_pub_right.publish(msg_right)
		rate.sleep()
		#cv2.imshow("left",left)
		#cv2.imshow("right",right)
		#cv2.waitKey(1)

main()
