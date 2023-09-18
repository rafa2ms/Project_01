from cv2 import *

cam_port = 0
cam = VideoCapture(cam_port)

result, image = cam.read()

if result:
	imshow("View",image)
	imwrite("View",image)

	waitKey(0)
	destroyWindow("View")

else:
	print("No image detected. Please, try again.")
