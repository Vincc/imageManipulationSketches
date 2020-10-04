import cv2
import numpy as np
import math


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
#generate thresholds:
IntensityArray = []
seg = math.gcd(img.shape[0],img.shape[1])
for i in range(seg**2):
    IntensityArray.append([])
sub = 0
mainsub = 0

###USER ADJUSTED
bias = 75
###

for rowCounter, row in enumerate(img):
    if rowCounter % (img.shape[0] / seg) == 0:
        if mainsub == seg-1:
            mainsub = 0
        else:
            mainsub += 1
    for pixelCounter,RGBpixel in enumerate(row):
        if pixelCounter % (img.shape[1]/seg) == 0:
            if sub == seg-1:
                sub = 0
            else:
                sub +=1
            IntensityArray[sub+(mainsub*seg)].append(np.sqrt(RGBpixel[0]**2+RGBpixel[1]**2+RGBpixel[2]**2))
temp = []

for i in IntensityArray:
    temp.append(int(sum(i)/len(i)))

#horizontal iteration
mainsub = 0
sub = 0




for rowc, row in enumerate(img):
    if rowc % (img.shape[0] / seg) == 0:

        if mainsub == seg-1:
            mainsub = 0
        else:
            mainsub += 1
    if rowc == img.shape[0]-1:
        continue
    for c,i in enumerate(row):

        if c % (img.shape[1] / seg) == 0:
            #print(temp[sub + (mainsub * seg)])
            if sub == seg - 1:
                sub = 0
            else:
                sub += 1
        if c == img.shape[1]-1:
            continue
        privtense = np.sqrt(int(row[c][0]**2) + int(row[c][1]**2) + int(row[c][2] ** 2))
        curtense = np.sqrt(int(row[c+1][0]**2) + int(row[c+1][1]**2) + int(row[c+1][2] ** 2))
        bottense = np.sqrt(np.square(int(img[rowc+1][c][0])) + int(np.square(img[rowc+1][c][1])) + int(np.square(img[rowc+1][c][2])))
        diffhor = curtense - privtense
        diffver = curtense - bottense
        diff = diffhor + diffver





        if  diff*2 > temp[sub+(mainsub*seg)]:
            try:

                row[c] = [255,0,0]
                blank[rowc][c] = [225, 0, 0]
            except IndexError:
                continue



cv2.imshow('image',blank)
cv2.waitKey(0)