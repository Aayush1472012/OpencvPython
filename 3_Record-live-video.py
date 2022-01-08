import cv2

# recording live video
vid = cv2.VideoCapture(0)   # Accessing Camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# VideoWriter(<filename>, <fourcc code>, <frames/sec>, <(width, height)>)
out = cv2.VideoWriter('output.mp4', fourcc, 20, (640, 480))

### if number of frame/sec is low then video will be slow and vice-versa.

while True:
    ret, frame = vid.read()
    # check for frame is readed or not
    if ret == True:
        out.write(frame)    # Writing frame to output file
        
        cv2.imshow('live video', frame)     # Display frames
        
        if cv2.waitKey(1) & 0xFF == ord('q'):   # Stop video when user enters 'q'
            break
    else:
        break

# release all resources
vid.release()
out.release()
# destroy all windows
cv2.destroyAllWindows()