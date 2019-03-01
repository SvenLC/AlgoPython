import math
from math import sqrt

def estPremier(n):
    if n <= 1:
        return False
    else:
        i = 2
        while i <= sqrt(n):
            if n % i == 0:
                return False
            i += 1
        return True


listePremier = []

for i in range (2, 100, 1):
    if estPremier(i):
        listePremier.append(i)

print(listePremier)

