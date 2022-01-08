# Schrijf een methode dat een doolhof accepteert (i.e., een 8x8-matrix van getallen 0 of 1).
# Een 0 geeft een vrije positie aan en een 1 geeft een muur aan. De posities (0, 0) en (7, 7) 
# zijn de start en stop posities en zijn openstaande posities. Zoek vanaf positie (0, 0)
#  een pad door het doolhof om bij locatie (7, 7) te komen. Alleen horizontale en verticale 
# bewegingen zijn toegestaan. Diagonale bewegingen zijn niet toegestaan en een verplaatsing
# tegen een muur is niet toegestaan. Zorg ervoor dat het algoritme eerder verkende paden vermijdt.

maze = [[0, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0]]


def examine(doolhof, doel, partial_solution):
    # Schrijf hier je functie die nakijkt of je partiële oplossing:
    # - Een acceptabele oplossing is voor het probleem (ACCEPT)
    # - Nog geen oplossing is, maar er wel nog een kan worden na uitbreiding (CONTINUE)
    # - Nooit nog een correcte oplossing kan worden voor het probleem (ABANDON)
    juist = 0
    fout = 0
    visited = []
    for i in partial_solution:
        if i not in visited:
            if doolhof[i[0]][i[1]] != 1:
                juist += 1
            else:
                fout += 1
            visited.append(i)
        else:
            fout += 1
    if juist == len(partial_solution) and partial_solution[-1] == doel:
        return 'Accept'
    elif fout > 0:
        return 'Abandon'
    else:
        return 'Continue'


def extend(doolhof, doel, partial_solution):
    # Schrijf hier je functie die een partiële oplossing uitbreidt
    possible_solutions = []
    x_range = partial_solution[-1][0]
    y_range = partial_solution[-1][1]
    if x_range != 0: #Vermijden dat we x-1 doen als hij op x=0 staat
        possible_solutions.append(partial_solution+[[x_range-1, y_range]])
    if y_range != 0: #Vermijden dat we y-1 doen als hij op y=0 staat
        possible_solutions.append(partial_solution+[[x_range, y_range-1]])
    if x_range != len(doolhof)-1: #Vermijden dat we x+1 doen als hij op x=7 staat
        possible_solutions.append(partial_solution+[[x_range+1, y_range]])
    if y_range != len(doolhof)-1: #Vermijden dat we y+1 doen als hij op x=7 staat
        possible_solutions.append(partial_solution + [[x_range, y_range+1]])
    return possible_solutions





def solve(doolhof, doel, partial_solution=[[0,0]], solutions = []):
    # Schrijf hier je functie die het probleem in z'n geheel oplost. Deze maakt gebruik van de examine-functie, van de
    # extend-functie en tenslotte ook van zichzelf (om de gegenereerde extensies op te lossen)
    exam = examine(doolhof, doel, partial_solution)
    if exam == 'Accept':
        solutions.append(partial_solution)
    elif exam != 'Abandon':
        for p in extend(doolhof, doel, partial_solution):
            solve(doolhof, doel, p, solutions)
    return solutions


print('x', solve(maze, [7, 7]))
doolhof1 =  [[0, 0, 0, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 1, 0]]
solutions = solve(doolhof1, [7, 7], [[0, 0]], [])
print(solutions)
assert [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [4, 4], [4, 5], [3, 5], [2, 5], [1, 5], [1, 6], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7]] in solutions
assert [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [5, 7], [6, 7], [7, 7]] in solutions
