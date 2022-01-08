"""
Schrijf een functie die het minimum aantal munten berekent dat nodig is om een bepaald
bedrag te betalen. Het bedrag en een lijst met mogelijke muntwaarden worden als argumenten
meegegeven.

Als de invoerlijst [1, 2, 5, 10, 20, 50] is, is het minimum aantal munten dat nodig is om
een bedrag van 67 te betalen gelijk aan 4 (namelijk 50 + 10 + 5 + 2).

Veronderstel het volgende bij het schrijven van de functie:
    1. Het invoerbedrag is een positief geheel getal verschillend van nul.
    2. De functie veronderstelt een niet-lege lijst met mogelijke muntwaarden.
    3. Ga ervan uit dat het opgegeven bedrag altijd kan worden betaald met de munten uit de
    gegeven lijst met waarden.
"""

def examine(bedrag, munten, partial_solution):
    if sum(partial_solution) == bedrag:
        return 'Accept'
    elif sum(partial_solution) > bedrag:
        return 'Abandon'
    else:
        return 'Continue'


def extend(bedrag, munten, partial_solution):
    partial_solutions = []
    for i in munten:
        partial_solutions.append(partial_solution + [i])
    return partial_solutions


def solve(bedrag, munten, partial_solution=[]):
    exam = examine(bedrag, munten, partial_solution)
    if exam == 'Accept':
        return [partial_solution]
    elif exam != 'Abandon':
        results = []
        #print(extend(bedrag, munten, partial_solution))
        for p in extend(bedrag, munten, partial_solution):
            solutions = solve(bedrag, munten, p)
            #print(solutions)
            for i in solutions:
                if sorted(i) not in results:
                    results.append(sorted(i))
            #print(results)
        return results
    return []

def min_amount_of_coins(bedrag, munten):
    lijst = solve(bedrag, munten)
    minimum = (len(lijst[0]), lijst[0])
    for i in lijst:
        if len(i) < minimum[0]:
            minimum = (len(i), i)
    return minimum

print(min_amount_of_coins(15, [1, 2, 5, 10, 20, 50]))
print(min_amount_of_coins(51, [1, 50]))
assert min_amount_of_coins(51, [1, 50])[0] == 2
assert min_amount_of_coins(23, [1, 2, 5, 10])[0] == 4
assert min_amount_of_coins(80, [5, 20, 50])[0] == 4
print(min_amount_of_coins(67, [1, 2, 5, 10, 20, 50]))