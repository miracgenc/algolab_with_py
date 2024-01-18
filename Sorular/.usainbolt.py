yaris = int(input(""))
puanlar = input().strip()
puanlar = puanlar.split(" ")
i = 0
while (i < len(puanlar)):
    puanlar[i] = int(puanlar[i])
    i+=1
i = 0
kirilanrekor = 0
rekor = puanlar[i]
while (i < len(puanlar)):
    if (rekor >= puanlar[i]):
        i+=1
    elif (rekor < puanlar[i]):
        kirilanrekor+=1
        rekor = puanlar[i]
        i+=1
print(kirilanrekor)