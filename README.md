# Episode 01
### Version 4.0 - Face and time Snapshot using OOP
This version is an upgrade of the image capture project (see main branch).<br/>
_Released on the 26th of September of 2023_ <br/>

## Goals
- [x] Enhance the main project using OOP
- [x] Make it a pyhton package
- [x] Add requirements.txt

## Requirements
 This library is running successfully under the following requirements:
- Python: 3.8.18
- OpenCV: 4.3.0.38
  - numpy==1.24.4

## How to use
1. Access your virtual environment or _$ cd_ to your project folder
``` bash
$ cd my/project/folder
```
2. Clone/Dowload this repository
``` bash
$ git clone https://github.com/rafa2ms/project_01.git
```
3. Install the requirements
``` bash
$ pip install -r requirements.txt
```
4. In your .py script, import the "modules" library
5. Call the desired functions
6. As soon as you run the script, a new window will open displaying the webcam snapshot.
   - The file will be saved with the name "Snapshot.png".
   - It will be saved in the same directory as your script.

### Example
The script bellow demonstrates a simple way to import the library and utilize the module functions. <br/>

``` python
import modules as mod
import cv2
import time

result, image = mod.init_cam()

if result is None:
	print("No image detected. Please, try again.")
else:
	mod.time_snapshot(image)
	mod.text_snapshot("Gruezi",image)
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
```

### Output
<img src = "https://github.com/rafa2ms/project_01/blob/oop_enhanced/Snapshot.png?raw=true" />
[Snapshot.png]

## Current output features
- [x] Time of capture <br/>
- [x] Multiple labels <br/>

## [SOLVED] Video capture error 
If your cam_port is not 0 (default), the following error will show up:
``` bash
[ WARN:0] global /tmp/pip-req-build-gnlqiqil/opencv/modules/videoio/src/cap_v4l.cpp (893) open VIDEOIO(V4L2:/dev/video0): can't open camera by index
```

### Ubuntu
1. Ask for video permission
``` bash
$ sudo adduser <your.device.name> video
$ sudo usermod -a --group video <your.device.name>
```

2. Check your permissions
``` bash
$ id -a
```

3. Copy index from groups (for me it's "1000")
``` bash
uid=1000(<your.device.name>) gid=1000(<your.device.name>) groups=1000(<your.device.name>) ...
```

4. Use that index as the parameter of the _time_snapshot()_ function:
``` python
import episode01 as ep
import cv2

ep.time_snapshot(cam_port=1000)
```
Source: https://stackoverflow.com/a/70281742/22612897

## References
1. https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
2. https://stackoverflow.com/questions/54607447/opencv-how-to-overlay-text-on-video
3. https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time
4. https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_programming
5. https://www.askpython.com/python/oops/init-method
