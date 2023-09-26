from cv2 import *
from .label_class import Label

# Initialize webcam. the cam port is a parameter once it may 
# change froom onen pc to another. By default, it is set to zero.

def init_cam(cam_port = 0):
    cam = VideoCapture(cam_port)
    result, image = cam.read()
    image = cv2.flip(image,1) # flip the image once its mirrored on the cam feed.
    
    return result, image


# Add a label with current time. Bydefault, this label
# will be add on the botton, centralized

def time_snapshot(image):
    height, width, channels = image.shape

    # Calculate the central position on the botton
    w = round(width/2)
    h = height-20
    
    time_label = Label(pos = (w,h), scale=0.8, align='C')
    time_label.set_time()
    time_label.draw_label(image)


# Add a text label. The content is a parameter, that
# by default is empty and the position is on the top-left.

def text_snapshot(txt = "", image = ""):
    text_label = Label(pos = (0,0), scale=0.8, align='L',text = txt)
    text_label.draw_label(image)


