# mouse event
# EVENT_FLAG_LBUTTON 1         # left clicking
# EVENT_MOUSEMOVE 0            # mouse moving
# EVENT_LBUTTONDBLCLK 7        # double left clicking


import cv2 as cv
import numpy as np

ox = 0
oy = 0



def signing(event, x, y, flags, param):
    global img
    global ox, oy, sx, sy

    if event == cv.EVENT_LBUTTONDBLCLK: # double click
        img = np.ones((500, 500, 3), np.uint8) * 100
    elif event != cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        ox, oy = x, y
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.line(img, (ox, oy), (x, y), (255, 255, 255), 3, cv.LINE_AA)
        ox, oy = x, y


# create a black image
img = np.ones((500, 500, 3), np.uint8)

# create window and set mouse call back function
cv.namedWindow("image")
cv.setMouseCallback('image', signing)


while True:
    cv.imshow("image", img)
    #k = cv.waitKey(25) & 0xFF
    #if chr(k) == 'q':
    #    break
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
        