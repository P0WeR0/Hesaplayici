#Bu program Github @P0WeR0 kullanıcısı tarafından yapılmıştır.

import time

print("                             Hesaplayıcı\n                          -----------------")

print("                      Seçebileceğiniz İşlemler:\n                   ------------------------------\nbölme,çarpma,çıkarma,toplama,üs-alma,sürat-hesaplama,ivme-hesaplama,yüzde-hesaplama\n----------------------------------------------------------------------------------\n                (Büyük, Küçük Harflere Duyarlıdır!)\n               -------------------------------------")

#tercih
i = input("Tercihinizi Giriniz: ")

#işlemler
çarp = "çarpma"
böl = "bölme"
çık = "çıkarma"
üs = "üs-alma"
sür = "sürat-hesaplama"
top =  "toplama"
iv = "ivme-hesaplama"
yüzde = "yüzde-hesaplama"

def Hesaplayıcı():
    #hesaplamalar
    if i == böl:
        print("Bölme Aracına Hoş Geldiniz.\n---------------------------")
        a = int(input("Bölünecek Sayıyı Giriniz: "))
        b = int(input("Bölen Sayıyı Giriniz: "))
        if (b == 0):
            print("Sıfıra Bölünemez! \n")
            time.sleep(3)
        elif (a < b): 
            print("Sonuç 0 Kalan ",b,"\n")
            time.sleep(3)
        elif (a > b):
            c = a // b
            d = a - c * b
            print('Sonuç =', c, 'Kalan =', d,"\n")
            time.sleep(3)
        elif (a == b):
            print("Sonuç = 1 Kalan = 0""\n")
            time.sleep(3)
    elif i == çarp:
        print("Çarpma Aracına Hoş Geldiniz.\n----------------------------")
        a = int(input("Çarpılacak 1. Sayıyı Giriniz: "))
        b = int(input("Çarpılacak 2. Sayıyı Giriniz: "))
        s = a * b
        print("Çarpım Sonucu =",s,"\n")
        time.sleep(3)
    elif i == çık:
        print("Çıkarma Aracına Hoş Geldiniz.\n-----------------------------")
        a = int(input("Çıkarılacak Sayıyı Giriniz: "))
        b = int(input("Çıkaracak Sayıyı Giriniz: "))
        s = a - b
        print("Çıkarma Sonucu =",s,"\n")
        time.sleep(3)
    elif i == top:
        print("Toplama Aracına Hoş Geldiniz.\n-----------------------------")
        a = int(input("Toplamacak 1. Sayıyı Giriniz: "))
        b = int(input("Toplanacak 2. Sayıyı Giriniz: "))
        s = a + b
        print("Toplam =",s,"\n")
        time.sleep(3)
    elif i == sür:
        print("Sürat Hesaplama Aracına Hoş Geldiniz.\n--------------------------------------")
        d = int(input("Mesafeyi Giriniz: "))
        t = int(input("Süreyi Giriniz: "))
        v = d / t
        print("Sürat =",v,"\n")
        time.sleep(3)
    elif i == üs:
        print("Üs Alma Aracına Hoş Geldiniz.\n-----------------------------")
        a = int(input("Tabanı Giriniz: "))
        b = int(input("Üssü Giriniz: "))
        s = a ** b
        print("Sonuç =",s,"\n")
        time.sleep(3)
    elif i == iv:
        print("İvme Hesaplama Aracına Hoş Geldiniz.\n-------------------------------------")
        a = int(input("Sürati Giriniz: "))
        b = int(input("Zamanı Giriniz: "))
        s = a / b
        print("İvme =",s,"\n")
        time.sleep(3)
    elif i == yüzde:
        print("Yüzde Hesaplama Aracına Hoş Geldiniz.\n--------------------------------------")
        y = int(input("Yüzdesi Alınacak Sayıyı Giriniz: "))
        b = int(input("Yüzde Sayısı: "))
        a = b / 100
        c = y * (a)
        print(c,"\n")
        time.sleep(3)
    else:
        print("------------------------------\nLütfen Seçiminizi Doğru Yapın!")
    return "tekrarla"

while Hesaplayıcı() == "tekrarla":
   Hesaplayıcı()
