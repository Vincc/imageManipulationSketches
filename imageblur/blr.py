import cv2
import numpy as np
img = np.asarray(cv2.imread('par.jpg'))
new = img
origarray = []
print(img.shape)
for RGBiteration in range(img.shape[2]):
    for rowindex,row in enumerate(img):
        if rowindex == 0 or rowindex == img.shape[0]-1:
            continue
        for c,i in enumerate(row):
            if c == 0 or c == img.shape[1]-1:
                continue
            new[rowindex][c][RGBiteration] = int((int(img[rowindex][c][RGBiteration])   +   int(img[rowindex-1][c][RGBiteration])   +   int(img[rowindex+1][c][RGBiteration])   +   int(img[rowindex][c-1][RGBiteration])   +   int(img[rowindex][c+1][RGBiteration])   +   int(img[rowindex-1][c-1][RGBiteration])   +   int(img[rowindex-1][c+1][RGBiteration])   +   int(img[rowindex+1][c-1][RGBiteration])   +   int(img[rowindex+1][c+1][RGBiteration]))/9)
cv2.imshow('image',new)
cv2.waitKey(0)