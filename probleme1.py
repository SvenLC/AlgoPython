# Je remplis une tirelire de la manière suivante:
# - Je commence par déposer 1€ dans la tirelire (un lundi)
# - Puis j'y dépose 2,01 € le jour suivant (un mardi)
# - Puis 3,02 € le jour suivant (un mercredi)
# - Puis 4,03 € le jour suivant (un jeudi)
# - etc, (chaque jou j'y dépose 1,01 de plus que la veille).
#     par exemple : le huitième jour (un lundi), j'y dépose 8,07 € et le contenu total
#     de la tirelire est : 1 + 2,01 + 3,02 + 4,03 + 5,04 + 6,05 + 7,06 + 8,07 = 36,28 €

# Lorsque le contenu total de la tirelire dépasse 1500 €, je casse la tirelire.

# Le but du sujet est de déterminer le contenu de la tirelire lorsque je la casserai.

def depot(n):
    if n == 1 :
        return 1
    else :
        return depot(n-1) + 1.01


def jour(n):
    jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    x = (n-1)%7
    return jours[x]

def contenu(t):
    s = 0
    for i in range(1, t, 1):
        s += depot(t)
    return s


i = 1
while contenu(i) <= 1500:
    i += 1

print('Je casserais la tirelire un ' + jour(i) + ' et son contenu sera de ' + str(contenu(i)))
