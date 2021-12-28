"""
Schrijf een iteratieve functie som_iteratief die de som van alle natuurlijke
getallen tot en met een gegeven getal berekent: som_iteratief(n) = 1 + 2 + 3 + ... + n.

Schrijf ook een recursieve functie som_recursief die dezelfde som berekent door
gebruik te maken van recursie.

Maak gebruik van assert statements om te controleren of je functies goed werken en
schrijf er documentatie bij.
"""


def som_iteratief(n):
    """

    @param n:
    @return:
    """
    sum = 0
    while n >= 1:
        sum +=  n
        n -= 1
    return sum

print(som_iteratief(10))


def som_recursief(n):
    # Vergeet ook bij deze functie geen documentatie te schrijven
    if n == 1:
        return 1
    else:
        return n+som_iteratief(n-1)

# Schrijf zelf enkele assert statements om je functies te testen

print(som_recursief(10))