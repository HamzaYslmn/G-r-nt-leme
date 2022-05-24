from lib2to3.pytree import convert
from random import gauss
import cv2
from cv2 import blur
from cv2 import bilateralFilter
import numpy as np              



img= cv2.imread("Goruntuisleme1/Resimler/kurukafa.png")
imgGri= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Kafa", imgGri)  

cv2.waitKey(0)
cv2.destroyAllWindows()
