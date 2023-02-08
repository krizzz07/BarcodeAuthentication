import numpy as np
import cv2
from pyzbar import pyzbar

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('auth.txt') as f:
    myDataList=f.read().splitlines()
while True:
    success, img = cap.read()
    for barcode in pyzbar.decode(img):
        print(barcode.data)
        myData=(barcode.data.decode('utf-8'))
        print(myData)

        if myData in myDataList:
            output=("Authentication success")
            mycolor=(0,255,0)
        else:
            output=("Authentication failed")
            mycolor=(0,0,255)
        pts = np.array([barcode.polygon],np.int32)
        pts.reshape(-1,1,2)
        cv2.polylines(img,[pts],True,mycolor,5)
        pts2=barcode.rect
        cv2.putText(img, output, (pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, mycolor, 2)


    cv2.imshow("Result", img)
    cv2.waitKey(1)
