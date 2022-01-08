import numpy as np
import cv2

# creating blank image of 512x512 using numpy array
img = np.zeros([512,512,3], dtype=np.uint8)

# shape function syntax = shapeName(<image>, <pt1>, <pt2>, <(B,G,R)>, <thickness>)
# if thickness = -1, then it will fill whole shape by given color.
img = cv2.line(img, (0,0), (255,255), (0,0,255), 2)
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 2)
img = cv2.rectangle(img, (384,0), (510,128), (255,255,0), 4)
# circle(<img>, <center>, <radius>, <(B,G,R)>, <thickness>)
img = cv2.circle(img, (447,63), 63, (0,255,255), -1)

# putText(<img>,<Text>,<pt>,<font>,<font_size>,<(B,G,R)>,<thickness>,<line_type>)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"OpenCV",(10,490),font,4,(255,255,255),5,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()