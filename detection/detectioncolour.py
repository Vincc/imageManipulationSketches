import cv2
import numpy as np
#required
 #pip install opencv-python
 #pip install numpy
 
img = np.asarray(cv2.imread('par.jpg'))
print(img.shape)
blank = img.copy()
for row in blank:
    for i in row:
        for x in i:
            x = [255, 255, 255]
for row in blank:
    for i in range(len(row)):
        row[i] = [255,255,255]
for rowc, row in enumerate(img):
    for c,i in enumerate(row):
        if c == img.shape[1]-1:
            continue
        privtense = np.sqrt(int(row[c][0]**2) + int(row[c][1]**2) + int(row[c][2] ** 2))
        curtense = np.sqrt(int(row[c+1][0]**2) + int(row[c+1][1]**2) + int(row[c+1][2] ** 2))
        diff = curtense - privtense
        a = 500
        if  diff**2 > a:
            try:
                for i in range(1):
                    row[c+i] = [255,0,0]
                    blank[rowc][c+i] = [255,0,0]
            except IndexError:
                continue


cv2.imshow('image',blank)
cv2.waitKey(0)