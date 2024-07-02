# Данный пример предназначен для симулятора!  

# В данном примере аппарат плывет вперед до тех пор, пока не будет остановлена программа. 
# Во время выполнения будут отображаться изображения с донной камеры и выделяться карсные объекты и их центры. 

# Функции get_image_front и get_image_bottom работают только в симуляторе. 
# Для получения видео на аппарате используйте cv2.VideoCapture из OpenCV!
# (https://docs.opencv.org/4.7.0/dd/d43/tutorial_py_video_display.html)


import pymurapi as mur
import cv2
import numpy as np


auv = mur.mur_init()

def detect_color_objects(image):
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_color = np.array([170,50,50])
    upper_color = np.array([180,255,255])
    mask = cv2.inRange(img_hsv, lower_color, upper_color)

    cv2.imshow("Image", mask)
    cv2.waitKey(5)
            


if __name__ == '__main__':
    while True:
        #detect_color_objects(auv.get_image_bottom())
        detect_color_objects(auv.get_image_front())
        
        
        
        
        
        
