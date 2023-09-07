import cv2

VIDEO_PATH = r"C:\Users\Namita\Downloads\toys_-_55015 (720p).mp4"
vid = cv2.VideoCapture(VIDEO_PATH)
while True:
    status, img = vid.read()
    if not status:
        print('video is not available')
        break
    # vision operations
    img = cv2.resize(img,None,fx=.25, fy=.25)
    cv2.imshow('Video', img)
    key = cv2.waitKey(25)
    if key == 27:
        break
cv2.destroyAllWindows()
vid.release()