"""
Ömer and Melih, the indomitable guardians of Turkey (of course, and inzva), are arguing over who is better at math.

Melih decides to ask Ömer a simple question to test his knowledge:

“How many different positive integers less than or equal to N can be written as p∗q^5 where q is a prime number and p is a positive integer smaller than or equal to q?”

In fact, Melih's aim is to make Ömer work and eat all the cookies in the house while he is dealing with this long process. Ömer, on the other hand, is sure that there is an algorithm that can easily solve this question. Help Ömer by writing the code that prints the answer for the given N.
"""




sayi = int(input(""))
i=2
k=1
liste = []

def asalmi(n):
    for i in range(2,int(n)):
        if n%i==0:
            return False
        
    return True

while((i**5) <= sayi):
    if (asalmi(i) == True):
        while(k <= i):
            if(k * (i**5) <= sayi):
                liste.append(k * (i**5))
            k+=1
        i+=1
        k=1
    else:
        i+=1

print(liste)