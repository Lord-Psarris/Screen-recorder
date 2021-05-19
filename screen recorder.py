import pyautogui
import cv2
import numpy as np
import os

print('started')

resolution = (1920, 1080)
_ = cv2.VideoWriter_fourcc(*'XVID')


def filename():
    file_name = "screen_record.avi"
    path = os.getcwd() + '\\' + file_name
    file, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = "screen_record_" + str(counter) + extension
        counter += 1

    return path


rate = 5

# Creating a VideoWriter object
out = cv2.VideoWriter(filename(), _, rate, resolution)

cv2.namedWindow("Screen recorder", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Screen recorder", 480, 270)

while True:
    # screenshot
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (1920, 1080))

    # Write it to the output file
    out.write(frame)

    # Optional: Display the screen
    cv2.imshow('Screen recorder', frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
