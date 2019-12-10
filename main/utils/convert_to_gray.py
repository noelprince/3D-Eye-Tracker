import numpy as np
import cv2 as cv
from sys import argv

cap = cv.VideoCapture(argv[1])
# Define the codec and create VideoWriter object
ret, frame = cap.read()
print("Dimensions:")
dim = np.array(frame).shape
print(dim)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
print("Frame height")
print(frame_height)
print("Frame width")
print(frame_width)
fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv.VideoWriter('outpy.avi', fourcc, 10,
                     (frame_width, frame_height))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
