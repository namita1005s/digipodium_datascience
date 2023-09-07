import cv2 # library version 4
# basic image filter -> grayscale,rgb,hsv.yuv,ycrcb,lab,luv,xyz
# adv image filter -> canny, laplacian,sobel,hough
CAM_IDX=0
cam=cv2.VideoCapture(CAM_IDX)
cv2.namedWindow("canny")
lowthreshold = cv2.createTrackbar("Low Threshold","canny",0,1000,lambda x:None)
highthreshold = cv2.createTrackbar("High Threshold","canny",0,1000,lambda x:None)
while cam.isOpened():
    state,img=cam.read()
    if not state:
        print('camera is not available')
        break
    im_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    im_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    lt= cv2.getTrackbarPos("Low Threshold","canny")
    ht= cv2.getTrackbarPos("High Threshold","canny")
    im_canny= cv2.Canny(img,lt,ht)
    im_sobel= cv2.Sobel(img,cv2.CV_64F,1,1,ksize=3)
    cv2.imshow('original',img)
    cv2.imshow('gray',im_gray)
    cv2.imshow('rgb',im_rgb)
    cv2.imshow('canny',im_canny)
    cv2.imshow('sobel',im_sobel)

    key=cv2.waitKey(10)
    if key==ord('q'):
        break
cv2.destroyAllWindows()
cam.release()
     