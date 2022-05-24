import imp
import cv2
import cv2
import numpy as np
from matplotlib import pyplot as plt

img= cv2.imread("Resimler/coklukafa.jpg",0) #grileştirdik

e,thresh1=cv2.threshold(img, 140,255,cv2.THRESH_BINARY ) 
e,thresh2= cv2.threshold(img,80,255,cv2.THRESH_BINARY_INV)
e,thresh3= cv2.threshold(img,80,255,cv2.THRESH_OTSU)
e,thresh4= cv2.threshold(img,80,255,cv2.THRESH_TOZERO)
e,thresh5= cv2.threshold(img,80,255,cv2.THRESH_TOZERO_INV)
e,thresh6= cv2.threshold(img,80,255,cv2.THRESH_TRUNC)
#80 altı siyah, üstündeki değerler beyaz


titlelist=["BINARY","BINARY_INV","OTSU", "TOZERO", "TOZERO_INV","TRUNC"]
imglist= [thresh1,thresh2,thresh3,thresh4,thresh5,thresh6]
 
for i in range(6): #6 resim olacak
    
    plt.subplot(2,3,i+1), plt.imshow(imglist[i],"gray",vmin=0,vmax=255) 
    #*2 satır 3 sütun 1. blok , resmi göster ilk elemanı, hepsini gri göster, 0 ve 255 arasında.
    
    plt.title(titlelist[i]) 
    #*resimlerin üstüne başlık yazdırma
    
    plt.xticks([]),plt.yticks([])
    #*Tıklanan noktlaraın X,Y değerlerinin görüntülenmesi
    
plt.show() #göster