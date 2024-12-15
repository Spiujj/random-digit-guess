import random 


while True:
    sayi=random.randint(0,10)

    giriş=input("lüten sayı girin: ")
    giriş1=int(giriş)

    if giriş1==sayi:
        print("Tebrikler, bildiniz!")
        print("Tahmin edilen sayı:", sayi)
        break
    else:
        print("Üzgünüm, bilemediniz!")
        print("Tahmin edilen sayı:", sayi)
