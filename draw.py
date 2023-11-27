from tracker import Tracker
import cv2
import imageio

tracker = Tracker()
cap = cv2.VideoCapture(0)
while True:
    flag, img = cap.read()
    if not flag: 
        break
    img = tracker.hand_landmark(img)
    img = tracker.tracking(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

