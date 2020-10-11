import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
count = 0
total = 10
folder_name = input("Enter Folder Name: ")

while(cap.isOpened()):
  ret, frame = cap.read()
  
  # Display the frame
  cv2.imshow('frame', frame)

  if ret == False:
    break
  
  # Save frame
  cv2.imwrite('../Face-Recognition/dataset/' + file_dir + '/' + str(i) + '.jpg', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

  # Check total and break
  count+=1
  if count == total:
    break

  time.sleep(0.5)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()