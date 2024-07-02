import cv2
import video
import numpy
if __name__ == '__main__':
    def nothing(*arg):
        pass
    
    cv2.namedWindow( "out_window" )
    cap = video.create_capture(0)
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    
    while True:
        flag, img = cap.read()
        
        height, width = img.shape[:2]
        edge = 10
        
        low_blue = numpy.array((90,20,20), numpy.uint8)
        high_blue = numpy.array((150,255,255), numpy.uint8)
        try:
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask_blue = cv2.inRange(img_hsv,low_blue, high_blue)
            
            #result = cv2.bitwise_and(img_hsv,img_hsv,mask = mask_blue)
            #result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
            
            moments = cv2.moments(mask_blue, 1)
            
            dM01 = moments['m01']
            dM10 = moments['m10']
            dArea = moments['m00']
  
            x=0
            
            if dArea > 150:
                x = int(dM10 / dArea)
                y = int(dM01 / dArea)
                cv2.circle(img, (x, y), 10, (255,0,0), -1)
            
            if (x>(width/2+edge)) and x!=0:
                cv2.rectangle(img, (0,0), (30,height), (0,255,0), -1)
            if (x<(width/2-edge)) and x!=0:
                cv2.rectangle(img, (width-30,0), (width,height), (0,255,0), -1)
                
            cv2.imshow("out_window", img)
        except:
            cap.release()
            raise
 
        ch = cv2.waitKey(50)
        #для выхода надо нажать esc
        if ch == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
