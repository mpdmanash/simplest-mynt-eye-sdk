import cv2
import sys
import numpy as np

def main():
	cap = cv2.VideoCapture(int(sys.argv[1]))
	cap.set(cv2.CAP_PROP_CONVERT_RGB, False)
	while True:
		ret,frame = cap.read()

		left = frame[:,:,0]
		right = frame[:,:,1]
		
		cv2.imshow("left",left)
		cv2.imshow("right",right)
		cv2.waitKey(1)



main()
