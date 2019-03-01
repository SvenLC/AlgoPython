import math
from math import sqrt

def estPremier(n):
    isPrime = True
    if n <= 1:
        return False
    elif 2 == n or 3 == n:
        return True
    else:
        i = 2
        while i <= sqrt(n) and isPrime == True:
            if n % i == 0:
                isPrime = False
            i += 1
        return isPrime


listePremier = []

for i in range (2, 100, 1):
    if estPremier(i):
        listePremier.append(i)

print(listePremier)

