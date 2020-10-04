import cv2
import numpy as np

a = []
img = np.asarray(cv2.imread('par.jpg'))
print(img.shape)
blank = img.copy()
for row in blank:
    for i in row:
        a.append(int(np.sqrt(i[0]**2+i[1]**2+i[2]**2)))
        for x in i:
            x = [255, 255, 255]
aa = int(sum(a)/len(a))
for row in blank:
    for i in range(len(row)):
        row[i] = [255,255,255]
#horizontal iteration
for rowc, row in enumerate(img):
    if rowc == img.shape[0]-1:
        continue
    for c,i in enumerate(row):
        if c == img.shape[1]-1:
            continue
        privtense = np.sqrt(int(row[c][0]**2) + int(row[c][1]**2) + int(row[c][2] ** 2))
        curtense = np.sqrt(int(row[c+1][0]**2) + int(row[c+1][1]**2) + int(row[c+1][2] ** 2))
        bottense = np.sqrt(np.square(int(img[rowc+1][c][0])) + int(np.square(img[rowc+1][c][1])) + int(np.square(img[rowc+1][c][2])))
        diffhor = curtense - privtense
        diffver = curtense - bottense
        diff = diffhor + diffver



        if  diff*1.5 > aa:
            try:
                for i in range(1):
                    row[c+i] = [255,0,0]
                    blank[rowc][c+i] = [255,0,0]
            except IndexError:
                continue


cv2.imshow('image',blank)
cv2.waitKey(0)