from lib2to3.pytree import convert
from random import gauss
import cv2
from cv2 import blur
from cv2 import bilateralFilter
import numpy as np                            
img= cv2.imread("Goruntuisleme1/Resimler/kurukafa.png")                   #*hangi resmi açıyoruz
imgGri= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)               #*grileştirme
cv2.imshow("Kafa", imgGri)                                 #*gri resmi açma

size_y=img.shape[0]
size_x=img.shape[1]
kanal =img.shape[2]         
#* X,Y boyutları ve Resmin Kanal sayısı. RGB 3, Gri Tek kanal

print("Yukseklik", size_y, "Genislik", size_x, "Kanal Sayisi", kanal)

print(imgGri[100,100])


blur=cv2.blur(imgGri,(5,5))                      #*blurlaştırma
cv2.imshow("Bulanikkafa", blur)                  #*görseli açma


gaus=cv2.GaussianBlur(imgGri,(5,5),0)            #*gaus keskinleştirme kenarlar bulanık
cv2.imshow("Gauskafa", gaus)


bilateral= cv2.bilateralFilter(imgGri,9,75,75)   #*biliteral keskinleştirme daha keskin kenar
cv2.imshow("Biliteralkafa", gaus)

median= cv2.medianBlur(imgGri,3)                 #(Tek sayı olmalı) #*Parazit azaltma filitresi
cv2.imshow("Mediankafa", median)


canny= cv2.Canny(imgGri,50,200)                  #*Alt ve üst Eşik değerine göre kenar seçme
cv2.imshow("Kenarkafa", canny)




cv2.waitKey(0)
cv2.destroyAllWindows()                          #*pencereyi kapatana kadar açık tut
