"""
Schrijf een functie die, gegeven een lijst met unieke elementen, een lijst met alle mogelijke permutaties
teruggeeft. De volgorde van de uitvoer maakt niet uit. Bij invoer [1,2,3] zou je als resultaat [[1,2,3],[1,3,2],[2,1,3],
[2,3,1],[3,1,2],[3,2,1]] kunnen krijgen. Wat kan je doen als de elementen in de lijst niet uniek zijn?
"""


# Voel je vrij om bij de gegeven structuur argumenten naar keuze mee te geven!

def examine(lijst, partial_solution):
    # Schrijf hier je functie die nakijkt of je partiële oplossing:
    # - Een acceptabele oplossing is voor het probleem (ACCEPT)
    # - Nog geen oplossing is, maar er wel nog een kan worden na uitbreiding (CONTINUE)
    # - Nooit nog een correcte oplossing kan worden voor het probleem (ABANDON)

    if sorted(lijst) == sorted(partial_solution):
        return 'Accept'
    elif len(partial_solution) > len(set(partial_solution)):
        return 'Abandon'
    else:
        return 'Continue'




def extend(lijst, partial_solution):
    # Schrijf hier je functie die een partiële oplossing uitbreidt
    result = []
    for i in lijst:
        result.append(partial_solution + [i])
    return result


def solve(lijst, partial_solution=[]):
    # Schrijf hier je functie die het probleem in z'n geheel oplost. Deze maakt gebruik van de examine-functie, van de
    # extend-functie en tenslotte ook van zichzelf (om de gegenereerde extensies op te lossen)
    exam = examine(lijst, partial_solution)
    if exam == 'Accept':
        return [partial_solution]
    elif exam != 'Abandon':
        solution = []
        for p in extend(lijst, partial_solution):
            if solve(lijst, p) is not None:
                for i in solve(lijst, p):
                    solution.append(i)
        return solution

print(solve([1, 2, 3, 4, 5, 6]))
