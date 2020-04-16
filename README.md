# Object-detection
Small OpenCV program that can detect object of set color and show its coordinates.

Program contains two pieces of code: main.py and SlidersC.C.

SlidersC.C is class that contains basic GUI for setting lower and upper HSV color bounderies for the mask. It also has few usefull buttons that can set red, green, blue and skin color instantly. 

Program detects color set in basic GUI using mask and put circle on found countour (or contours). The center of the circle is showed as the center of detected object(s).

Program is fully described in comments in the code.
