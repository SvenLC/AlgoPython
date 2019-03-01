listeNbPair = []

def estPaire(n):
    if n % 2 == 0:
        return True
    else:
        return False


for i in range(1,100,1):
    if estPaire(i):
        listeNbPair.append(i)

print(listeNbPair)
