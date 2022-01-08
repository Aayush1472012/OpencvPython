import cv2
import datetime

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    dateTime = str(datetime.datetime.now())     # getting current time
    font = cv2.FONT_HERSHEY_SIMPLEX     # selecting font type
    frame = cv2.putText(frame, dateTime, (10,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
    cv2.imshow('video',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()