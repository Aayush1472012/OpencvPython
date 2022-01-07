# Importing opencv library
import cv2

print("Vesrion of OpenCV:",cv2.__version__)      # printing version of opencv


# Reading & Displaying an Image
img1 = cv2.imread("Resources/image1.jpg")    # Reading an image in normal mode
img2 = cv2.imread("Resources/image1.jpg", 0) # Reading an image in grayscale mode
window_name1 = 'image1'      # Name of image window
window_name2 = 'image2'      # Name of image window
cv2.imshow(window_name1, img1)     # Display an image
cv2.imshow(window_name2, img2)     # Display an image
cv2.waitKey(0)      # Adding Delay to display image for longer time (waits for user to press any key)
cv2.destroyAllWindows()     # Destroying all image windows


# Reading & Displaying Video
vid = cv2.VideoCapture("Resources/video1.")