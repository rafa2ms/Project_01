from cv2 import *
from datetime import datetime


def draw_label(img,text,pos,align, bg_color):
	font_face = cv2.FONT_HERSHEY_SIMPLEX
	scale = 1
	color = (0, 0, 0)
	thickness = cv2.FILLED
	margin = 10
	txt_size = cv2.getTextSize(text, font_face, scale, thickness)
	
	pos_x = pos[0]

	if align == 'c':
		pos_x = pos[0] - round(txt_size[0][0]/2)
	
	end_x = pos_x  + txt_size[0][0] + margin
	end_y = pos[1] - txt_size[0][1] - margin
	
	cv2.rectangle(img, (pos_x, pos[1] + margin), (end_x, end_y), bg_color, thickness)
	cv2.putText(img, text, (pos_x, pos[1]), font_face, scale, color, 1, cv2.LINE_AA)

cam_port = 0
cam = VideoCapture(cam_port)

result, image = cam.read()

if result:
	datetime_now = datetime.now()
	time_now = str (datetime_now.time())
	#print(time_now[0:8])
	#test = "hello"
	
	height, width, channels = image.shape
	w = round(width/2)
	h = height-20
	#print(w,h)

	draw_label(image,time_now[0:8], (w,h),'c', (200,213,48))
	imshow("View",image)

	imwrite("View.png",image)

	waitKey(0)
	destroyWindow("View")

else:
	print("No image detected. Please, try again.")
