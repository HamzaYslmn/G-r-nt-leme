from lib2to3.pytree import convert
from random import gauss
import cv2
from cv2 import blur
from cv2 import bilateralFilter
import numpy as np              



img= cv2.imread("Resimler/kurukafa.png",0)                    #? Flags 0 olduğunda Griye çeviriyor
                                                              #imgGri= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                                              #bu şekilde de griye çevrilebilir

cv2.imwrite("Resimler/GriKafa.png", img)                      #* İstenen yere resmi Kaydetmeye yarar
cv2.imshow("Kafa", img)  













cv2.waitKey(0)
cv2.destroyAllWindows()

"""
k=cv2.waitKey(0)          #* istenen tuşa (q) basıldığında komut gerçekleştirme
if k=='q'
"""