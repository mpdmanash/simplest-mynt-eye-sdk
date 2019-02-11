import cv2
import sys
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import rospy

bridge = CvBridge()

def main():
	cap = cv2.VideoCapture(int(sys.argv[1]))
	cap.set(cv2.CAP_PROP_CONVERT_RGB, False)
	rospy.init_node("talker", anonymous=True)
	pub_l = rospy.Publisher("stereo/left/image", Image, queue_size=10)
	pub_r = rospy.Publisher("stereo/right/image", Image, queue_size=10)
	rate = rospy.Rate(25) # 25hz
	while not rospy.is_shutdown():

		ret,frame = cap.read()

		left = frame[:,:,0]
		right = frame[:,:,1]
		left = cv2.resize(left,(640,480))
		right = cv2.resize(right,(640,480))

		try:
		
			left_msg = bridge.cv2_to_imgmsg(left, "mono8")
			left_msg.header.stamp = rospy.Time.now()
			pub_l.publish(left_msg)

			right_msg = bridge.cv2_to_imgmsg(right, "mono8")
			right_msg.header.stamp = rospy.Time.now()
			pub_r.publish(right_msg)
			rate.sleep()
		except CvBridgeError as err:
			print err

        # cv2.imshow("left",left)
        # cv2.imshow("right",right)
        # cv2.waitKey(1)
        


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
    	pass
