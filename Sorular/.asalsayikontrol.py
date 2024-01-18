sayi = int(input("Sayı giriniz"))
sayac = 2

if (sayi <= 1):
    print("Sayının asallığı kontrol edilemez")
    exit

while (sayac < sayi):
    if (sayi % sayac == 0):
        print("Sayı asal değildir")
        break
    sayac+=1

if (sayac == sayi):
    print(sayi, "Sayısı asaldır")