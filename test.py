import cv2
import numpy as np 


camera_params = np.load("ik_cam(480x360).npz")

newcameramtx = camera_params["newcameramtx"]
roi = camera_params["roi"]
mtx = camera_params["mtx"]
dist = camera_params["dist"]

stream = cv2.VideoCapture(0)

RUN = True

if __name__ == "__main__":

    while RUN:
        ret, img = stream.read()
        img = cv2.resize(img, (480, 360))
        undistort = cv2.undistort(img, mtx, dist, None, newcameramtx)
        x,y,w,h = roi
        undistort2 = undistort[y:y+h, x:x+w]
        print(dist)
        if ret:
            cv2.imshow('undistort', undistort)
            cv2.imshow('undistort2', undistort2)
            cv2.imshow('original', img)
            if cv2.waitKey(10) & 0xFF == 27:
                RUN = not RUN
        else:
            print("Can't read data from camera!")
            RUN = not RUN
