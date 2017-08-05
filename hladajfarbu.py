import cv2
import numpy as np
backsub = cv2.BackgroundSubtractorMOG()
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# hranice filtra
    lower_red = np.array([10,90,10])
    upper_red = np.array([254,200,100])
# maskovanie obrazu
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)
# detekcia zmeny
    fgmask = backsub.apply(mask, None,0.001)
    contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# velkost videa spravi5 automatiku
    Y = 480
    X = 640
# rozdelenie obrazu
    cv2.line(frame,(0,Y/2),(X,Y/2),(255,0,255),1)
    cv2.line(frame,(X/2,0),(X/2,Y),(255,0,255),1)
    try: hierarchy = hierarchy[0]
    except: hierarchy = []
    for contour, hier in zip(contours, hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w > 20 and h > 20:
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
                    x1 = w/2      
                    y1 = h/2
                    cx = x+x1
                    cy = y+y1

                    if cx > X/2 :
                        if cy > Y/2:
                            print("pravo dole")
                        else :
                            print("pravo hore")
                    else :
                        if cy > Y/2:
                            print("vlavo dole")
                        else :
                            print("vlavo hore")
                    centroid = (cx,cy)
                    cv2.circle(frame,(int(cx),int(cy)),2,(0,0,255),-1)
                    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
