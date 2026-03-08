# PROJECT 2:Coin Counter : This program counts the number of coins displayed on the screen
# importiing libraries
import cv2 as cv # opencv library
import numpy as np #numpy library to convert the ecimal value of HoughCircles to int
from collections import deque # for temporal smoothing
url='http://192.168.0.147:8080/video' # ip webcam this can change
cap=cv.VideoCapture(url) #read the vedio

count=0 # declaring the count variable
while (1):
    success,img=cap.read()
    img=cv.resize(img,(640,480))
    # convert each image of the vediio to gray-> blur->canny
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),6)
    canny=cv.Canny(blur,100,200,3)
    cv.imshow("canny",canny) # to show canny is working
    # defing circles
    circles = cv.HoughCircles(
        canny,
        cv.HOUGH_GRADIENT,
        dp=1.2,
        minDist=50,
        param1=100,
        param2=30,
        minRadius=20,
        maxRadius=80
    )
    if circles is not None:
     circles=np.uint16(np.around(circles)) # convert the decimal value given by HoughCircles to int
     count = len(circles[0]) #increasing the count variable
     #drawing the detected circles
     for i in circles[0,:]:
        cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        cv.circle(img,(i[0],i[1]),2,(0,255,0),3)
    #displaying the number of counts
    count_history=deque(maxlen=15)
    count_stable=0
    count_history.append(count)
    count_stable=round(sum(count_history)/len(count_history))
    cv.putText(img,f'{count_stable}',(20,40),2,2,(0,0,0),2)
    # showing the image
    #cv.imshow("image",img)
    cv.imshow("detected circles",img)
    # exit command
    if cv.waitKey(1) & 0xFF==ord('d'):
        cv.destroyAllWindows()
        break