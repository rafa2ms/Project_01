# Episode 01
### Version 3.0 - Face and time Snapshot using OOP
This version is an upgrade of the image capture project (see main branch).<br/>
_Released on the 21th of September of 2023_ <br/>

## Goals
- [x] Enhance the main project using OOP
- [x] Make it a pyhton package
- [x] Add requirements.txt

## How to use
1. As soon as you run the script, a new window will open displaying the webcam snapshot.
   - The file will be saved with the name "Snapshot.png".
   - It will be saved in the same directory as your script.
2. To exit the project, press the "escape" key.

### Example
The script bellow demonstrates a simple way to import the library and utilize the "time_snapshot()" function. <br/>
_Note: Using infinite loop may cause issues in your code._

``` python
import episode01 as ep
import cv2

ep.time_snapshot()

while True:
    k = cv2.waitKey(30) & 0xff
    if k ==27: break
```


## Requirements
 This library is running successfully under the following requirements:
- Python: 3.8.18
- OpenCV: 4.3.0.38
  - numpy==1.24.4

## Current output features
- [x] Time of capture <br/>
- [x] Multiple labels <br/>

## Examples of labeling
``` python 
label_1 = Label(text = "OOP provides", txt_color=(0,0,255), scale=0.6)
label_1.draw_label(image)

label_2 = Label(text = "easier data", pos = (20, 45), margin=5, font_face=cv2.FONT_HERSHEY_TRIPLEX,
                txt_color=(255,255,255), bg_color=(0,0,255), scale=0.8)
label_2.draw_label(image)

label_3 = Label(text = "manipulation", pos = (60, 85), margin=10, font_face=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                txt_color=(0, 231, 255), bg_color=(73, 158, 0), scale=1)
label_3.draw_label(image)
```
<img src = "https://github.com/rafa2ms/episodes/blob/oop_scratch/Snapshot.png?raw=true" />
[Snapshot.png - "Creative mode!"]

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
