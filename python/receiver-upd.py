import numpy as np 
import cv2 
from multiprocessing import Process

def receive():
    print("receive()")
    #cap_receive = cv2.VideoCapture('udpsrc port=5000 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! decodebin ! videoconvert ! appsink', cv2.CAP_GSTREAMER)
    
    #cap_receive = cv2.VideoCapture('udpsrc port=5000 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! h264parse ! decodebin ! videoconvert ! appsink', cv2.CAP_GSTREAMER)
    
    cap_receive = cv2.VideoCapture('udpsrc port=5000 ! gdpdepay ! rtph264depay ! h264parse ! decodebin ! videoconvert ! appsink', cv2.CAP_GSTREAMER)

    print(cap_receive)
    if not cap_receive.isOpened():
        print('VideoCapture not opened')
        exit(0)

    while True:
        ret,frame = cap_receive.read()

        if not ret:
            print('empty frame')
            break

        cv2.imshow('receive', frame)
        if cv2.waitKey(1)&0xFF == ord('q'):
            break

    #cap_receive.release()

if __name__ == '__main__':
    #s = Process(target=send)
    r = Process(target=receive)
    #s.start()
    r.start()
    #s.join()
    r.join()

    cv2.destroyAllWindows()

