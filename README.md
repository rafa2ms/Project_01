# Episode 01
Version 1.0 - _released on the 18th of September of 2023_ <br/><br/>
This project is the first of a series of introductory challenges.<br/>
It was created to apply basic concepts of multiple tools and environments simultaneously.

## Goals
- [x] Capture an image from my webcam and show it in a window. <br/>
- [x] Add the time of capture as an overlay text. <br/>
- [ ] Run it with Python 3.9 and OpenCV 4.3.0.18 <br/>

## Requirements
 The code 'scratch.py' is running successfully under the following requirements:
- _Ubuntu 22.04 on Windows Subsystem for Linux (WSL2)_
- _Python: 3.8.18_
- _OpenCV: 4.0.3.38_

## Current output features
- [x] Time of capture <br/>
- [ ] Face detection _(soon)_ <br/>

<img src = "https://github.com/rafa2ms/episodes/blob/main/Final_result.png?raw=true" />

## Bugs 
The following error is related to the OpenCV 4.3 installation procedure. As there was another error during the installation from a cloned repository, now I'm trying to build the package. <br/>

``` bash
fatal error:
 opencv2/core/quaternion.hpp: No such file or directory
    9 | #include "opencv2/core/quaternion.hpp"
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
```

## Improvements 
As the program is working with no GUI to set parameters, there are many improvement possibilities for the future.

## References
1. https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
2. https://stackoverflow.com/questions/54607447/opencv-how-to-overlay-text-on-video
3. https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time
