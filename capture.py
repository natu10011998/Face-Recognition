import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
i = 0
j = 10

while(cap.isOpened()):
  ret, frame = cap.read()
  # Display the frame
  cv2.imshow('frame',frame)
  # Wait for 25ms
  if ret == False:
    break
  cv2.imwrite('../Face-Recognition/test_cap/' + str(i) + '.jpg',frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  i+=1
  time.sleep(0.5)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()