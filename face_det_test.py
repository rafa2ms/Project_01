import cv2
import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

#Aligment options
#	(l)eft
#	(c)enter
#	(r)ight

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
	# Convert to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 	# Detect the faces
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	# Draw the rectangle around each face
	n_face = 0

	for (x, y, w, h) in faces:
		##index = np.random.randint(0, len(color))
		tup = tuple(c[n_face])
		rgb = (int(tup[0]), int(tup[1]) ,int(tup[2]))
		rgb = color[n_face]
		cv2.rectangle(img, (x, y), (x+w, y+h), rgb, 2)
		# draw_label(img, "Face "+str(n_face), (x, y+h), 'l', c)
		# Display
		cv2.imshow('img', img)
		n_face = n_face + 1

	# Stop if escape key is pressed
	k = cv2.waitKey(30) & 0xff
	if k==27:
		break
# Release the VideoCapture object
cap.release()


# REFERENCE
# https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
