from cv2 import *
from datetime import datetime

class Label:
    def __init__(self, 
                font_face   = cv2.FONT_HERSHEY_SIMPLEX,
                scale       =  1,
                txt_color   = (0,0,0),
                bg_color    = (255,255,255),
                thickness   = cv2.FILLED,
                margin      = 10,
                pos         = (0,0),
                text        = "",
                align       = 'L'):
        
        self.font_face  = font_face  
        self.scale      = scale
        self.txt_color  = txt_color
        self.bg_color   = bg_color
        self.thickness  = thickness
        self.margin     = margin
        self.pos        = pos
        self.text       = text
        self.align      = align
    
    def set_time(self):
        datetime_now = datetime.now()
        self.text = str(datetime_now.time())
        self.text = self.text[0:8]
    

    def alignment(self):
        txt_size = cv2.getTextSize(self.text, self.font_face, self.scale, self.thickness)

        pos_x, pos_y = self.pos
        txt_length, txt_height = txt_size[0]

        if self.align == 'L':
            pos_x += self.margin
            pos_y += txt_height + self.margin

        elif self.align == 'C':
            pos_x -= round(txt_length/2)

        elif self.align == 'R':
            pos_x -= (txt_length + self.margin)
            pos_y += txt_height + self.margin

        end_x = pos_x + txt_length + self.margin
        end_y = pos_y - txt_height - self.margin

        return pos_x, pos_y, end_x, end_y 
    

    def draw_label(self,img):
        pos_x, pos_y, end_x, end_y = self.alignment()
        
        cv2.rectangle(img, (pos_x - self.margin, pos_y + self.margin), (end_x, end_y), self.bg_color, self.thickness)
        cv2.putText(img, self.text, (pos_x, pos_y), self.font_face, self.scale, self.txt_color, 1, cv2.LINE_AA)


