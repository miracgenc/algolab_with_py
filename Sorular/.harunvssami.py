# https://algoleague.com/problem/harun-and-sami/detail



tursayisi = input("")
tursayisi = tursayisi.split(" ")
for i in range(len(tursayisi)):
    tursayisi[i] = int(tursayisi[i])


turlar = str(input(""))
h= 0
s = 0

for i in range(len(turlar)):
    if ((turlar[i]) == "H"):
        h+=1
        i+=1
    elif ((turlar[i]) == "S"):
        s+=1
        i+=1


if (h > s):
    if((s + (tursayisi[0]-tursayisi[1])) < h):
        print("Harun")
    else:
        print("Cilek")

elif (s > h):
    if((h + (tursayisi[0]-tursayisi[1])) < s):
        print("Sami")
    else:
        print("Cilek")

elif (s == h):
    print("Cilek")

