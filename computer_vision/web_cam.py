import cv2 # library version 4
#CREATE A VIDEOCAPTURE OBJECT
CAM_IDX = 0
cam = cv2.VideoCapture(CAM_IDX)#create a videocapture object

while cam.isOpened(): #loop until the camera is available
   status, img = cam.read() #read the frame/image
   if status:
       cv2.imshow('Webcam',img) #display the frame/image
       key = cv2.waitKey(10) #wait for key press
       if key == 27:         #if the key pressed is ESC
         break              #exit the loop
   else:
    print('webcam is not available')
    break
# free up resources
cv2.destroyAllWindows()
cam.release()