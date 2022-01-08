# Aim: if user enter 'q' then just close the image and if user enter 's' then first saves the gray 
# scale image & then close it
import cv2

img = cv2.imread("Resources/lena.jpg", 0)
cv2.imshow('lena', img)
k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.jpg', img)
    cv2.destroyAllWindows()
