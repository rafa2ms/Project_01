import cv2
from datetime import datetime
import numpy as np
from datetime import datetime

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def draw_label(img,text,pos,txt_type, bg_color):
	font_face = cv2.FONT_HERSHEY_SIMPLEX
	color = (0, 0, 0)
	thickness = cv2.FILLED
	margin = 10
	
	pos_x = pos[0]
	pos_y = pos[1]

	if txt_type == 'time':
		scale = 1
		txt_size = cv2.getTextSize(text, font_face, scale, thickness)
		pos_x = pos_x - round(txt_size[0][0]/ 2)
	else:
		scale = 0.7
		txt_size = cv2.getTextSize(text, font_face, scale, thickness)
		pos_y = pos_y + txt_size[0][1] + margin
		pos_x = pos_x + margin
	
	end_x = pos_x + txt_size[0][0] + margin
	end_y = pos_y - txt_size[0][1] - margin
	
	cv2.rectangle(img, (pos_x - margin, pos_y + margin), (end_x, end_y), bg_color, thickness)
	cv2.putText(img, text, (pos_x, pos_y), font_face, scale, color, 1, cv2.LINE_AA)
	

color = [(230, 25, 75),
	(60, 180, 75),
	(255, 225, 25),
	(0, 130, 200),
	(245, 130, 48),
	(145, 30, 180),
	(70, 240, 240),
	(240, 50, 230),
	(210, 245, 60),
	(128, 128, 128)]

c = np.random.randint(0, 256,size=(10,3))

while True:

	# Read the frame
	_, img = cap.read()
	img = cv2.flip(img, 1)
	
	# Convert to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Detect the faces
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	# Draw the rectangle around each face
	n_face = 0

	datetime_now = datetime.now()
	time_now = str (datetime_now.time())
	height, width, channels = img.shape
	draw_label(img,time_now[0:8], (round(width/2),(height-20)),'time', (200,213,48))
	
	for (x, y, w, h) in faces:
		##index = np.random.randint(0, len(color))
		tup = tuple(c[n_face])
		rgb = (int(tup[0]), int(tup[1]) ,int(tup[2]))
		rgb = color[n_face]
		cv2.rectangle(img, (x, y), (x+w, y+h), rgb, 2)
		draw_label(img, "Face "+str(n_face+1), (x, y+h), 'label', rgb)
		
		n_face = n_face + 1

        # Display
	cv2.imshow('Face and time', img)
		
	k = cv2.waitKey(30) & 0xff

	# Stop if escape key is pressed
	if k==27:
		break

	# Snapshot if space key is pressed
	if k==32:
		cv2.imwrite("Snapshot_at_" + (time_now[0:8]).replace(":","-")+ ".png",img)
		print("Snapshot successfully saved!")

# Release the VideoCapture object
cap.release()


# REFERENCE
# https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
