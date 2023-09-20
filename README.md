# Episode 01
### Version 2.0 - Face Detection
This version is an upgrade of the image capture project _(see main branch)_.<br/>
 _Released on the 20th of September of 2023_ <br/>

## Goals
- [x] Detect faces using a webcam. <br/>
- [x] Add a label for each face as an overlay text. <br/>
- [x] Show each label with a specific color. <br/>
- [x] Add the time of capture as an overlay text. <br/>
- [ ] Run it with Python 3.9 and OpenCV 4.3.0.18 <br/>

## Requirements
 The code 'face_det_test.py' is running successfully under the following requirements:
- _Ubuntu 22.04 on Windows Subsystem for Linux (WSL2)_
- _Python: 3.8.18_
- _OpenCV: 4.3.0.38_

## Current output features
- [x] Time of capture <br/>
- [x] Face detection <br/>

<img src = "https://github.com/rafa2ms/episodes/blob/face_detection/Snapshot_at_11-29-13.png?raw=true" /> <br/>
_<Snapshot_at_11-29-13.png - "My three different personalities">_

## How to use 
- As soon as you run the script, a new window will open displaying the current capture from the connected webcam.
- To take a __snapshot__ you should press the "space bar" key.
   - The file name will be "Snapshot_at_hh-mm-ss.png", where hh-mm-ss stands for the "hour", "minute" and "second" when the capture was done.
   - It will be saved on the same directory where "face_det_test.py" is running.
- To __quit the project__ you need to press the "escape" key.

## References
1. https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
2. https://stackoverflow.com/questions/54607447/opencv-how-to-overlay-text-on-video
3. https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time
4. https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
