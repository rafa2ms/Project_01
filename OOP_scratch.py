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

        '''
        elif align == 'R':
            pos_x = pos_x - round(txt_size[0][0]/ 2)
        '''
        
        end_x = pos_x + txt_size[0][0] + self.margin
        end_y = pos_y - txt_size[0][1] - self.margin
        
        cv2.rectangle(img, (pos_x - self.margin, pos_y + self.margin), (end_x, end_y), self.bg_color, self.thickness)
        cv2.putText(img, self.text, (pos_x, pos_y), self.font_face, self.scale, self.txt_color, 1, cv2.LINE_AA)

cam_port = 0
cam = VideoCapture(cam_port)

while True:
    result, image = cam.read()
    image = cv2.flip(image,1)

    if result:
        
        height, width, channels = image.shape
        w = round(width/2)
        h = height-20
        
        time_label = Label(pos = (w,h), scale=0.8, align='C')#bg_color = (200,213,48)
        time_label.set_time()
        time_label.draw_label(image)
        
        label_1 = Label(text = "OOP provides", txt_color=(0,0,255), scale=0.6)
        label_1.draw_label(image)

        label_2 = Label(text = "easier data", pos = (20, 45), margin=5, font_face=cv2.FONT_HERSHEY_TRIPLEX,
                        txt_color=(255,255,255), bg_color=(0,0,255), scale=0.8)
        label_2.draw_label(image)
        
        label_3 = Label(text = "manipulation", pos = (60, 85), margin=10, font_face=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                        txt_color=(0, 231, 255), bg_color=(73, 158, 0), scale=1)
        label_3.draw_label(image)

        imshow("View",image)

        #imwrite("View.png",image)

    else:
        print("No image detected. Please, try again.")

    k = cv2.waitKey(30) & 0xff
    if k ==27: break
    if k ==32: imwrite("Snapshot.png",image)