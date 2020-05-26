import cv2
import numpy as np

cap= cv2.VideoCapture("red_panda_snow.mp4")

fourcc = cv2.VideoWriter_fourcc(*"XVID") # To save video
out= cv2.VideoWriter("Flipped_red_panda.avi",fourcc, 25 ,(640,360)) # Video will not save here in .mp4 so use .avi
while True:
    ret, frame= cap.read()
     # to check video(frame) resolution size
#    print(frame.shape)
    frame2 = cv2.flip(frame,1)  # flip the video 0 for vertical and 1 for horizontal

    cv2.imshow("flipping",frame2)
    cv2.imshow("frame", frame)

    out.write(frame2)

    key= cv2.waitKey(30)
    if key==27:
        break

out.release()
cap.release()
cv2.destroyAllWindows()