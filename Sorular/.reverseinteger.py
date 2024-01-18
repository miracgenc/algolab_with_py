sayi=int(input("Sayı girin"))
gecicisayi = 0
basamak = 0
sonucsayi = " "

if (sayi >= 0):
    uzunluk = len(str(sayi))
elif (sayi < 0):
    uzunluk = len(str(sayi))-1

if (sayi == 0):
    print("0")

elif (sayi > 0):
    while (basamak < uzunluk):
        gecicisayi = int(sayi / 10)
        sonucsayi = str(sonucsayi) + str(sayi % 10)
        sayi = gecicisayi
        basamak+=1

elif (sayi < 0):
    sayi = -(sayi)
    sonucsayi = "-"
    while (basamak < uzunluk):
        gecicisayi = int(sayi / 10)
        sonucsayi = str(sonucsayi) + str(sayi % 10)
        sayi = gecicisayi
        basamak+=1

print(sonucsayi)
    