import numpy as np
import cv2

# create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5px
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Draw shapes
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# Polygan
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
img = cv2.polylines(img, [pts], True, (0, 255, 255))

# Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyWindow('image')


#################### mouse as a paint brush ####################
# mouse callback function
def draw_circle (event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
# create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()


################ Trackbar as the Color Palette ################
