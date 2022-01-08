"""
Gegeven n, schrijf een functie die alle combinaties van n paren goed gevormde haakjes genereert
door gebruik te maken van backtracking. Hiermee wordt bedoeld dat elk openend haakje ook
terug gesloten wordt en vice versa. Voor n = 3 bijvoorbeeld, kunnen we als uitvoer de lijst
["((()))", "(()())", "(())()", "()(())", "()()()"] verwachten.
"""


def examine(n, partial_solution):
    if partial_solution.count('(') == partial_solution.count(')') == n:
        return 'Accept'
    elif partial_solution.count(')')>partial_solution.count('(') or partial_solution.count('(') > n or partial_solution.count(')')>n:
        return 'Abandon'
    else:
        return 'Continue'


def extend(n, partial_solution):
    part = []
    for i in "()":
        part.append(partial_solution + i)
    return part


def solve(n, partial_solution=""):
    exam = examine(n, partial_solution)
    if exam == 'Accept':
        return [partial_solution]
    elif exam != 'Abandon':
        solutions = []
        for p in extend(n, partial_solution):
            if solve(n, p) is not None:
                for i in solve(n, p):
                    solutions.append(i)
        return solutions


print(solve(3))
