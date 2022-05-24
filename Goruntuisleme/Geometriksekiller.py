import cv2
         



img= cv2.imread("Resimler/kurukafa.png")#?,0)   #? Flags 0 olduğunda Griye çeviriyor   
                                                #? renk gri olduğunda renkli çizgi çekilmiyor
                                               
                                               
                                               #imgGri= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                               #bu şekilde de griye çevrilebilir
                                               

cv2.line(img,(0,0),(300,300),(10,10,10),5)   #*çizgi
                                             #*cv2.line(img,(nerden),(nereye),(çizgi rengi),kalınlık)


cv2.rectangle(img, (50,50),(300,200),(0,50,255),3) # Dikdörtgen, #?thickness -1 olursa içi dolu olur

cv2.circle(img, (100,100),(100),(20,50,150),-1)    #Çember

cv2.ellipse(img, (100,200),(100,200),0,0,180,(120,50,0),2) #elips

cv2.putText(img, "OPEN CV" , (0,250),cv2.FONT_HERSHEY_SIMPLEX,2,(100,0,100),3,cv2.LINE_AA, True)

cv2.imshow("GriKafa",img)




cv2.waitKey(0)
cv2.destroyAllWindows()