
class yeniSinif():  #Sinif tanimlama
    pass            #hata vermeden gec

def Calisan1():
    kabiliyetleri=["Basketbol","Futbol"]
    unvani="Sporcu"
    print(kabiliyetleri)
    print(unvani)

Calisan1()

class Calisan2():
    kabiliyetleri=["Basketbol","Futbol","Tenis"]
    unvani="Sporcu"
    print(kabiliyetleri)
    print(unvani)
    
print(Calisan2.kabiliyetleri)      
Calisan2.isim="Tugba"
print(Calisan2.isim)
Calisan2.yas=21
print(Calisan2.yas)

#Goruldugu gibi fonksiyonlari cagirmadan calistiramiyorken sinif da oyle bir sey soz konusu degildir.

sesli_harfler="aeıioöuüAEIİOÖÜU"
sayac=0
kelime=input("Bir kelime giriniz:")

def sesliMi(harf):
    return harf in sesli_harfler

for harf in kelime:
    if sesliMi(harf):
        sayac+=1

print(f"{kelime} kelimesinin icinde {sayac} tane sesli harf vardir.")

