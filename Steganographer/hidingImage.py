import cv2
import numpy as np
bigSpoon = np.asarray(cv2.imread('lake.jpg')).copy()
smallSpoon = np.asarray(cv2.imread('cliff.jpg')).copy()
for cr, row in enumerate(smallSpoon):
    for ci, i in enumerate(row):
        # print(int(len(bigSpoon) / len(smallSpoon)))
        # bigSpoon[int(len(bigSpoon) / len(smallSpoon) * cr)][int(len(bigSpoon[0]) / len(smallSpoon[0]) * ci)] += i
        for ui, x in enumerate(i):
            try:
                bigSpoon[(3*cr)+ui][(3*ci)+ui][2] += x
            except IndexError:
                pass

print(bigSpoon)
cv2.imshow('image',bigSpoon)

cv2.waitKey(0)



