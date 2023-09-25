birinci=0
ikinci=1
basamak= int(1)
toplam = 0

# 1 1 2 3 5   

while True:
    sayac=input("Fibonnacci Sayı dizisinin kaçıncı basamağını bulmak istersiniz?")

    if(sayac =="exit"):
       break

    elif (int(sayac) < 1):
        print("Geçerli bir sayı giriniz")

    elif int(sayac) == 1:
     print("Fibonnacci sayısı dizisinin 1. basamağı 1")

    elif (int(sayac) > 1):
        print("Fibonnacci sayısı dizisinin 1. basamağı 1")
        while (basamak+1 <= int(sayac)):
            toplam = int(birinci) + int(ikinci)
            birinci = int(ikinci)
            print(f"Fibonnacci sayısı dizisinin {basamak+1}. basamağı {toplam}")
            ikinci = toplam
            basamak+=1
    basamak=1
    birinci=0
    ikinci=1