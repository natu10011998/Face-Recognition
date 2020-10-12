import numpy as np
import cv2
import time
import os
import shutil
import sys

cap = cv2.VideoCapture(0)
count = 0
total = 10
parent_dir = "../Face-Recognition/dataset/"
folder_name = input("Enter Folder Name: ")

if os.path.exists(parent_dir + folder_name):
  print("Folder already exists. Do you want to delete it and re-create?")
  choice = input("0. No\n1. Yes\nYour choice: ")
  choice = int(choice)
  if choice == 1:
    shutil.rmtree(parent_dir + folder_name, ignore_errors=True)
    os.mkdir(parent_dir + folder_name)
  else:
    print("Close tools ...")
    sys.exit()
else:
  os.mkdir(parent_dir + folder_name)

print("Starting Capture ...")

while(cap.isOpened()):
  ret, frame = cap.read()
  
  # Display the frame
  cv2.imshow('frame', frame)

  if ret == False:
    break
  
  # Save frame
  cv2.imwrite(parent_dir + file_dir + '/' + str(count) + '.jpg', frame)
  print("Capture {}/{}".format(count + 1, total))

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

  # Check total and break
  if count == total:
    break
  
  count += 1
  time.sleep(0.5)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()