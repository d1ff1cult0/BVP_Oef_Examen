"""
Schrijf een recursieve functie die de som over een gegeven lijst gehele getallen
berekent. Gebruik geen iteratie, noch de ingebouwde functie om dit te berekenen.

Hint: Je mag wel de functie len gebruiken om te kijken hoeveel elementen je lijst
bevat.
"""

def som_lijst(lijst):
    if len(lijst) == 1:
        return lijst[0]
    else:
        return lijst[0]+som_lijst(lijst[-(len(lijst)-1):])

print(som_lijst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
list_example = [3, 8, 16, 14, 12, 5, 10, 1]
print(som_lijst(list_example))
assert som_lijst(list_example) == sum(list_example)
print(sum(list_example))
