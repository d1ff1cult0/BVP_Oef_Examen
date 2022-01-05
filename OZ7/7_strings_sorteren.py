"""
Schrijf een functie sort_strings dat een lijst van strings sorteert op basis van hun lengte. Een string van lengte 2 zal dus eerder in de lijst staan dan een string van lengte 5.
"""
def sort_strings(lijst):
    sorted = 1
    # We gebruiken bubble_sort
    while sorted > 0:
        sorted = 0
        for i in range(len(lijst)-1):
            if len(lijst[i]) > len(lijst[i+1]):
                lijst[i], lijst[i+1] = lijst[i+1], lijst[i]
                sorted += 1
    return lijst

assert(sort_strings(["Appel", "Banaan", "Citroen", "Pompelmoes", "Kiwi"]) == ["Kiwi", "Appel", "Banaan", "Citroen", "Pompelmoes"])
assert(sort_strings(["Ajuin", "Aardappel", "Champignon", "Artisjok", "Radijs"]) == ["Ajuin", "Radijs", "Artisjok", "Aardappel", "Champignon"])
