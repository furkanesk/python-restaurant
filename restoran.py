import os
masalar = dict()
for i in range(10):
    masalar[i] = 0
def hesapekle():
    a = int(input("Masa no: "))
    if a < 10:
        eklenecek = int(input("Eklenecek ücret: "))
        masalar[a] = eklenecek + masalar[a]
        input("Yeni işlem için enter")
    else:
        print("Böyle bir masa yok.")
        input("Yeni giriş için enter")
def hesapsil():
    a = int(input("Masa no: "))
    if a < 10:
        eklenecek = int(input("Çıkarılan ücret: "))
        masalar[a] = masalar[a] - eklenecek
        input("Yeni işlem için enter")
    else:
        print("Böyle bir masa yok.")
        input("Yeni giriş için enter")
def dosyaekle(dosya_adi):
    try:
        dosya = open(dosya_adi)
        veriler = dosya.read()
        veriler = veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag = True
    except FileNotFoundError:
        flag = False
    if flag:
        for i in enumerate(veriler):
            masalar[i[0]] = int(i[1])
    else:
        pass
def guncelle():
    dosya = open("kayit.txt","w")
    for i in range(10):
        ucret = str(masalar[i])
        dosya.write(ucret + "\n")
    dosya.close()
dosyaekle("kayit.txt")
while True:

    os.system("cls")
    print("""
    [1] Masaları görüntüle
    [2] Hesap ekle
    [3] Hesap sil
    [4] çıkış
    """)

    secim = input("seçim yapınız: ")
    if secim == "1":
        for i in masalar:
            print("Masa {} = {}".format(i,masalar[i]))
        input("Yeni işlem için enter")
    elif secim == "2":
        hesapekle()
    elif secim == "3":
        hesapsil()
    elif secim == "4":
        guncelle()
        quit()
    else:
        print("Hatalı giriş yaptınız")
