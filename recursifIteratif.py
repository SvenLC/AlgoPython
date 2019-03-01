# Récursif
def ajouterUn(x, y):
    if x == y:
        return x
    else:
        return ajouterUn(x+1, y)

print(ajouterUn(1, 10))

# Itératif boucle for
def ajouterDeux(x, y):
    for i in range(0,10,1):
        x += 2
    
    return x

def ajouterDeux(x, y):
    i = 0
    while i <= y:
        x += 2
    
    return x

print(ajouterDeux(1,10))

# Itératif boucle while
listeNbPair = []
i = 1

def estPair(n):
    if n % 2 == 0:
        return True
    else:
        return False


while len(listeNbPair) <= 10 :    
    if estPair(i):
        listeNbPair.append(i)
    i += 1

print(listeNbPair)