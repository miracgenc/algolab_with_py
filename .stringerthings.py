uzunluk = int(input(""))
kelime = str(input(""))
yenikelime = str("")
i = 0
while i < (len(kelime)):
    if (i+1) == len(kelime):
        yenikelime = yenikelime + kelime[i]
        break
    elif kelime[i] == kelime[i+1]:
        i+=1
    elif kelime [i] != kelime[i+1]:
        yenikelime = yenikelime + kelime[i]
        i+=1
print(yenikelime)
    