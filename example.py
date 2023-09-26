import episode01 as ep
import cv2
import time

result, image = ep.init_cam()

if result is None:
	print("No image detected. Please, try again.")
else:
	ep.time_snapshot(image)
	ep.text_snapshot("Gruezi",image)
	cv2.imshow("View",image)

	period = 0
	time_initial = time.time()
	
	while True:
		k = cv2.waitKey(30) & 0xff
		if k == 27: break
		
		current_time = time.time()
		period = current_time - time_initial
		if period > 2: break
		
		time.sleep(1) # avoid excessive CPU usage

	cv2.imwrite("Snapshot.png",image)
