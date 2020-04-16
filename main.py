# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import SlidersC


# sliders object that have sliders and buttons
sliders = SlidersC.Sliders()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())
# setting font
font = cv2.FONT_HERSHEY_SIMPLEX
pts = deque(maxlen=args["buffer"])
# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	vs = VideoStream(src=0).start()
# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])
# allow the camera or video file to warm up
time.sleep(2.0)

while True:
	# grab the current frame
	frame = vs.read()
	# handle the frame from VideoCapture or VideoStream
	frame = frame[1] if args.get("video", False) else frame
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	# construct a mask for color set by sliders, then perform
	# a series of erosions to remove any small
	# blobs left in the mask
	sliders.update_slider()
	mask = cv2.inRange(hsv, sliders.get_lower_values(), sliders.get_upper_values())
	mask = cv2.erode(mask, None, iterations=2)
	# show the mask
	cv2.imshow("mask", mask)
	# find contours in the mask and draw them
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cv2.drawContours(frame, cnts, -1, (0, 0, 255), 3)
	center = None
	M = [] #moments table
	rad = [] #radiuses table
	center = []	#centers table
	x = [] #x and y tables
	y = []
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		#loop over the founded contours
		for cnts_num in range(len(cnts)):
			((t_x, t_y), t_rad) = cv2.minEnclosingCircle(cnts[cnts_num])	#get contour parameters into temp variables
			x.append(t_x)	#put parameters into tables
			y.append(t_y)
			rad.append(t_rad)
			M.append(cv2.moments(cnts[cnts_num])) #creating image moments and puting them into the table
			#protection from "m00" parameter being "0" e.g. if segmentation would have failed
			if M[cnts_num]["m00"] != 0:
				center.append((int(M[cnts_num]["m10"] / M[cnts_num]["m00"]), int(M[cnts_num]["m01"] / M[cnts_num]["m00"])))
			else :
				break
		# only proceed if the radius meets a minimum size (to limit noises)
			if rad[cnts_num] > 20:
				# draw the circle on the frame,
				cv2.circle(frame, (int(x[cnts_num]), int(y[cnts_num])), int(rad[cnts_num]),
					(0, 255, 255), 2)
			#add coordinates onto frame
			cv2.putText(frame, "x" + str(cnts_num) + ": " + str(round(x[cnts_num],2)) + " y" + str(cnts_num) + ": " + str(round(y[cnts_num],2)), (int(x[cnts_num]), int(y[cnts_num])), font, .6, (255, 255, 255), 2, cv2.LINE_AA)

	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
# if we are not using a video file, stop the camera video stream
if not args.get("video", False):
	vs.stop()
# otherwise, release the camera
else:
	vs.release()
# close all windows
cv2.destroyAllWindows()