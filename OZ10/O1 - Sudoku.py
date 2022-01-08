# Implementeer een programma die een oplossing berekent 
# voor mini-sudoku aan de hand van backtracking.

# Tip: Definieer helperfuncties en gebruik ze in je oplossing
# (bijvoorbeeld voor de kolom- en rijbeperkingen, of het bord een oplossing bevat, etc.).

# Extra: Breid je oplossing uit zodat je ook n × n-sudokus (met n gelijk aan 3, 4, 9, etc.) 
# kan oplossen. (Voeg de subraster-beperking toe en pas je code aan zodat je borden van een 
# willekeurig dimensie toelaat.)

mini_sudoku = [[0, 2, 0], [3, 1, 0], [0, 3, 0]]


def examine(zijde_lengte, partial_solution):
    # Schrijf hier je functie die nakijkt of je partiële oplossing:
    # - Een acceptabele oplossing is voor het probleem (ACCEPT)
    # - Nog geen oplossing is, maar er wel nog een kan worden na uitbreiding (CONTINUE)
    # - Nooit nog een correcte oplossing kan worden voor het probleem (ABANDON)
    rijen_correct = 0
    dubbels = 0
    for i in partial_solution:
        if 0 not in i and len(i) == len(set(i)) == zijde_lengte:
            rijen_correct += 1
        for k in range(1, zijde_lengte+1):
            if i.count(k) > 1:
                dubbels += 1

    kolommen_correct = 0
    for i in range(len(partial_solution)):
        kolom = []
        for j in range(len(partial_solution)):
            kolom.append(partial_solution[j][i])
        if 0 not in kolom and len(kolom) == len(set(kolom)) == zijde_lengte:
            kolommen_correct += 1
        for k in range(1, zijde_lengte + 1):
            if kolom.count(k) > 1:
                dubbels += 1

    if kolommen_correct == rijen_correct == zijde_lengte:
        return 'Accept'
    elif dubbels != 0:
        return 'Abandon'
    else:
        return 'Continue'


def extend(zijde_lengte, partial_solution):
    # Schrijf hier je functie die een partiële oplossing uitbreidt
    possible_solutions = []
    for i in range(len(partial_solution)):
        for j in range(len(partial_solution)):
            if partial_solution[i][j] == 0:
                for k in range(1, zijde_lengte + 1):
                    if k not in partial_solution[i]:
                        k_not_in = 0
                        for m in range(len(partial_solution)):
                            if partial_solution[m][j] != k:
                                k_not_in += 1
                        if k_not_in == len(partial_solution):
                            partial_solution[i][j] = k
                            possible_solutions.append(partial_solution)
    return possible_solutions


def solve(zijde_lengte, partial_solution):
    # Schrijf hier je functie die het probleem in z'n geheel oplost. Deze maakt gebruik van de examine-functie, van de
    # extend-functie en tenslotte ook van zichzelf (om de gegenereerde extensies op te lossen)
    exam = examine(zijde_lengte, partial_solution)
    if exam == 'Accept':
        return [partial_solution]
    elif exam != 'Abandon':
        solutions = []
        for i in extend(zijde_lengte, partial_solution):
            for j in solve(zijde_lengte, i):
                if j not in solutions:
                    solutions.append(j)
        return solutions
    return []

print(solve(3, mini_sudoku))
