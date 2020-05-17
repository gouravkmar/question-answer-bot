import cv2
import os
import numpy as np
import random
img = cv2.imread('/home/gourav/Downloads/image2.jpeg')
#grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

#binarize 
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
#cv2.imshow("hughu",thresh)
cv2.waitKey(0)

#find contours
im2,ctrs = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#print(ctrs)
#sort contours


sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
s=1
f=random.randrange(0,100000,1)
os.mkdir(r'/home/gourav/Desktop/aries/testbot/ocr/'+str(f))
for i, ctr in enumerate(sorted_ctrs):
    if(cv2.contourArea(ctr)>20):
        
    # Get bounding box
        
        x, y, w, h = cv2.boundingRect(ctr)
        print(x,y)
        # Getting ROI
        roi = img[y-3:y+h+3, x-3:x+w+3]
        #cv2.imshow("sffs",roi)
        #cv2.waitKey(0)

        # show ROI
        #cv2.imwrite('roi_imgs.png', roi)

        #cv2.imshow('charachter'+str(i), roi)
        #print("jkjj")
        #cv2.rectangle(img,(x,y),( x + w, y + h ),(90,0,255),2)
        #image=cv2.rectangle(img,(x,y),( x + w, y + h ),(90,0,255),2)
        #crop_img = img[y-10:y+h+10, x-10:x+w+10]
        
        os.chdir(r'/home/gourav/Desktop/aries/testbot/ocr/'+str(f))
        cv2.imwrite(str(s)+".jpg",roi)
        #cv2.imwrite(str(s)+".jpg",crop_img)
        s=s+1
        

       # image=cv2.resize(image,(500,500))
#         cv2.imshow("image",image)
#         cv2.waitKey(100)
#         cv2.destroyAllWindows()

#imae=cv2.resize(img,(500,500))
#cv2.imshow('marked areas',img)

#cv2.waitKey(0)
