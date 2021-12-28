"""
Schrijf een recursieve functie macht die x tot de macht n berekent. Je mag ervan
uitgaan dat n een natuurlijk getal is. Denk goed na over het basisgeval en controleer
of de functie ook werkt voor n = 0. Vermijd het gebruik van lussen.

Hint: een macht druk je uit in Python door gebruik te maken van de ** operator.
Zo geldt dat 2**3 in Python gelijk is aan 2³.
"""

def macht(x, n):
    if n == 0:
        return 1
    else:
        return x * macht(x, n-1)

print(macht(3, 3))

