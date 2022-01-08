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
cv2.waitKey(0)  # Adding Delay to display image for longer time (waits for user to press any key) (1=1ms & 0=infinite)
cv2.destroyAllWindows()     # Destroying all image windows



# Reading & Displaying a Video
vid = cv2.VideoCapture("Resources/vid1.mp4")   # reading video from specified path
window_name = 'video'

while True:     # Using for loop to display all the frames of video
    success, img = vid.read()   # reading one by one frame of video
    cv2.imshow(window_name, img)    # displaying frame in specified frame
    if cv2.waitKey(1) & 0xFF == ord('q'):   # condition for stoping video (Enter 'q' for quit video)
        break



# Accessing Web Camera of PC
live_vid = cv2.VideoCapture(0)  # Accessing web cam using its id(0)
live_vid.set(3,680)     # setting width of live video using its id(3)
live_vid.set(4,480)     # setting height of live video using its id(4)
live_vid.set(10,100)     # setting brightness of live video using its id(10)
window_name = 'video'

while True:     # Using for loop to display all the frames of video
    success, img = live_vid.read()   # reading one by one frame of video
    cv2.imshow(window_name, img)    # displaying frame in specified frame
    if cv2.waitKey(1) & 0xFF == ord('q'):   # condition for stoping video (Enter 'q' for quit video)
        break