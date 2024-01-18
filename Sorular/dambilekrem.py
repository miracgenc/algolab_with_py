sayi=input("").strip()
sayi=sayi.split(" ")
agirliklar = input("").strip()
agirliklar = agirliklar.split(" ")
i = 0
while (i < len(agirliklar)):
       agirliklar[i] = int(agirliklar[i])
       i+=1
i = 0 
while (i < len(sayi)):
       sayi[i] = int(sayi[i])
       i+=1

i=0
y=0
toplam=0

while (i < sayi[1]):
        LveR = input("").strip()
        LveR = LveR.split(" ")
        while (y < len(LveR)):
               LveR[y] = int(LveR[y])
               y+=1
        x = int(LveR[0])
        while x <= int(LveR[1]):
               toplam = toplam + (agirliklar[x-1])
               x+=1
        LveR = ""
        i+=1
        print(toplam)
        toplam=0

