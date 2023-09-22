from cv2 import *
from datetime import datetime

class Label:
    def __init__(self, 
                font_face = cv2.FONT_HERSHEY_SIMPLEX,
                scale = 1,
                txt_color = (0,0,0),
                bg_color = (255,255,255),
                thickness = cv2.FILLED,
                margin = 10,
                pos = (0,0),
                text = "",
                align = 'L'):
        
        self.font_face = font_face  
        self.scale = scale
        self.txt_color = txt_color
        self.bg_color = bg_color
        self.thickness = thickness
        self.margin = margin
        self.pos = pos
        self.text = text
        self.align = align
    
    def set_time(self):
        datetime_now = datetime.now()
        self.text = str(datetime_now.time())
        self.text = self.text[0:8]
        
    def draw_label(self,img):
        txt_size = cv2.getTextSize(self.text, self.font_face, self.scale, self.thickness)

        pos_x = self.pos[0]
        pos_y = self.pos[1]

        if self.align == 'L':
            pos_y = pos_y + txt_size[0][1] + self.margin
            pos_x = pos_x + self.margin
            
        elif self.align == 'C':
            pos_x = pos_x - round(txt_size[0][0]/ 2)

        elif self.align == 'R':
            pos_y = pos_y + txt_size[0][1] + self.margin
            pos_x = pos_x - txt_size[0][0]
        
        
        end_x = pos_x + txt_size[0][0] + self.margin
        end_y = pos_y - txt_size[0][1] - self.margin
        
        cv2.rectangle(img, (pos_x - self.margin, pos_y + self.margin), (end_x, end_y), self.bg_color, self.thickness)
        cv2.putText(img, self.text, (pos_x, pos_y), self.font_face, self.scale, self.txt_color, 1, cv2.LINE_AA)


# Better set cam_port as a parameter, once it may change from
# one pc to another. However, let's suppose that the port #zero
# is the most common and set it as default

def time_snapshot(cam_port = 0):
    cam = VideoCapture(cam_port)

    result, image = cam.read()
    image = cv2.flip(image,1)

    if result:
        
        height, width, channels = image.shape
        w = round(width/2)
        h = height-20
        
        time_label = Label(pos = (w,h), scale=0.8, align='C')
        time_label.set_time()
        time_label.draw_label(image)

        imshow("View",image)
        imwrite("Snapshot.png",image)

    else:
        print("No image detected. Please, try again.")


