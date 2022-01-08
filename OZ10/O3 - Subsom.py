# Schrijf een recursief programma dat een tupel getallen retourneert uit de gegeven reeks
# waarvan het totaal gelijk is aan de gegeven som. De functie retourneert None als zo een
# tupel niet kan worden gevormd.

#Bijvoorbeeld: Voor de lijst [5, 13, 23, 9, 3, 3] en doelsom 28, zou je pro- gramma (13, 9, 3, 3)
# of (5, 23) als oplossing moeten retourneren. Voor doelsom 46 op dezelfde lijst zou het None
# moeten retourneren.

def examine(partial_solution, doelsom, lijst):
    # Schrijf hier je functie die nakijkt of je partiële oplossing:
    # - Een acceptabele oplossing is voor het probleem (ACCEPT)
    # - Nog geen oplossing is, maar er wel nog een kan worden na uitbreiding (CONTINUE)
    # - Nooit nog een correcte oplossing kan worden voor het probleem (ABANDON)
    if sum(partial_solution) == doelsom:
        return 'Accept'
    elif sum(partial_solution) < doelsom-min(lijst):
        return 'Continue'
    else:
        return 'Abandon'


def extend(partial_solution, lijst):
    # Schrijf hier je functie die een partiële oplossing uitbreidt
    solutions = []
    for i in lijst:
        if lijst.count(i) > partial_solution.count(i):
            solutions.append(partial_solution + [i])
    return solutions


def solve(doelsom, lijst, partial_solution):
    # Schrijf hier je functie die het probleem in z'n geheel oplost. Deze maakt gebruik van de examine-functie, van de
    # extend-functie en tenslotte ook van zichzelf (om de gegenereerde extensies op te lossen)
    exam = examine(partial_solution, doelsom, lijst)
    if exam == 'Accept':
        return [partial_solution]
    elif exam != 'Abandon':
        solutions = []
        for p in extend(partial_solution, lijst):
            for i in solve(doelsom, lijst, p):
                if sorted(i) not in solutions:
                    solutions.append(sorted(i))
        return solutions
    return []

def subsom(doelsom, lijst, partial_solution=[]):
    solution = solve(doelsom, lijst, partial_solution)
    if not solution:
        return None
    else:
        new_sol = []
        for i in solution:
            new_sol.append(tuple(i))
        return new_sol


print(subsom(28, [5, 13, 23, 9, 3, 3]))
print(subsom(46, [5, 13, 23, 9, 3, 3]))
