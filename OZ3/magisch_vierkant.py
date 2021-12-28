"""
Een n * n-matrix is een magisch vierkant als de som van de elementen in elke
rij, elke kolom en over de twee diagonalen hetzelfde is. Schrijf een programma
dat, gegeven een matrix met 16 getallen, berekent of het om een magisch vierkant
gaat of niet. Je mag de matrix hier direct in een variabele plaatsen en hoeft
deze dus niet op te vragen aan de gebruiker.

Hint: Gebruik aparte for-lussen om na te kijken of alle kolommen, rijen en diagonalen tot hetzelfde getal sommeren.
"""

magisch_vierkant = [[16, 3, 2, 13],
                    [5, 10, 11, 8],
                    [9, 6, 7, 12],
                    [4, 15, 14, 1]]

geen_magisch_vierkant = [[16, 3, 2, 13],
                        [5, 10, 8, 11],
                        [9, 6, 7, 12],
                        [4, 15, 14, 1]]

# Schrijf je code hieronder
def is_magisch_vierkant(vierkant):
    rij1_som = sum(vierkant[0])
    rijen_gelijk = 0
    kolommen_gelijk = 0
    for i in range(len(vierkant)):
        if sum(vierkant[i]) == rij1_som:
            rijen_gelijk += 1
    for i in range(len(vierkant)):
        kolom_som = 0
        for j in range(len(vierkant)):
            kolom_som += vierkant[j][i]
        if kolom_som == rij1_som:
            kolommen_gelijk += 1
    sum_diagonal1 = 0
    sum_diagonal2 = 0
    for i in range(len(vierkant)):
        sum_diagonal1 += vierkant[i][i]
        sum_diagonal2 += vierkant[-i][-i]
    if rijen_gelijk == kolommen_gelijk == len(vierkant[0]) and sum_diagonal1 == sum_diagonal2 == rij1_som:
        print('Dit is een magisch vierkant!')
    else:
        print('Dit is geen magisch vierkant :(')

is_magisch_vierkant(magisch_vierkant)
is_magisch_vierkant(geen_magisch_vierkant)
