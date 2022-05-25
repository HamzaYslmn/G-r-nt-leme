from keras.models import Sequential        #* ysa modeli için.

from keras.layers import Dense             #* katmanlar oluşturabilmek için.

from termcolor import cprint               #* Çıktıları renklendirmek için.

import numpy                               #* Matris işlemleri için

#! cuda çekirdekleri lazım

""" 
 800 insanın vucudundan alınmış 8 değer var. 
 Bunlar; hamilelik sayısı, plazma glukoz konsantrasyonu, diastolic kan basıncı, 
 deri kalınlığı, kullanılan insulin miktarı, vucut kitle indexi, diyabet soyağacı ve yaş değerleridir. 
 
 Eğer son sütun 1 ise kişinin şeker hastası(diabet) olduğu, 0 ise diabet hastası olmadığı anlamına gelmektedir. 
"""
dataset = numpy.loadtxt("..\Diyabet\diyabet.csv", delimiter=",")

X = dataset[:600, 0:8]  #* işlenecek veriler 600 tane ve 8 sütun
Y = dataset[:600, 8]    #* 0 - 1 (sonuc sutununu tanımlıyoruz)


model = Sequential()    #*sırayla bağlı katmanlar olusturma işlemi
"""
Dense : bir katmandaki dügümler diger katmandaki bütün dügumlere bagli olacak
20 : perceptron sayısı (20 nöron)
input_dim = girdi sayısı
"""
model.add(Dense(20, input_dim=8, init='uniform', activation='relu'))

# İkinci katmanda 14 yapay sinir hücresi.
model.add(Dense(14, init='uniform', activation='relu'))

# Üçüncü katmanda 6 yapay hücremiz var.
model.add(Dense(6, init='uniform', activation='sigmoid'))

# Dördüncü katmanda 2 yapay hücremiz var. Çıkış
model.add(Dense(2, init='uniform', activation='sigmoid'))

# Derleme
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

"""
epoch : tur - deneme sayısı
batch : her seferde alınacak veri sayısı
verbose : hata olusursa goster
"""

model.fit(X, Y, nb_epoch=150, batch_size=10,  verbose=2)
# Başarı yüzdesi hesaplama
scores = model.evaluate(X, Y)

# basarı ölcutu ( dogruluk - kesinlik )
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


test_verisi = dataset[600:696, 0:8]    #* 96 adet test verimizin sonuc sutunu haric ilk 8 sutun (degerler) ornek olarak veriliyor.


tahminler = model.predict(test_verisi) #* Kişinin diyabet hastası olup olmadıgını tahmini

dogru = 0
yanlis = 0
toplam_veri = len(dataset[600:696, 8])

# veri setindeki gercek sonucları ve tahmin sonuclarını kıyaslama
for x, y in zip(tahminler, dataset[600:696, 8]):
    x = int(numpy.round(x[0]))      # degeri 0' yada 1' yuvarlar
    if int(x) == y:
        cprint("Tahmin: " + str(x) + " - Gerçek Değer: " + str(int(y)), "grey", "on_green", attrs=['bold'])
        dogru += 1
    else:
        cprint("Tahmin: " + str(x) + " - Gerçek Değer: " + str(int(y)), "grey", "on_red", attrs=['bold'])
        yanlis += 1

print("\n", "-" * 50, "\nISTATISTIK:\nToplam ", toplam_veri, " Veri içersinde;\nDoğru Bilme Sayısı: ", dogru,
      "\nYanlış Bilme Sayısı: ", yanlis,
      "\nBaşarı Yüzdesi: ", str(int(100 * dogru / toplam_veri)) + "%", sep="")