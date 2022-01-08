"""
Gegeven twee integers n en k, geef alle mogelijke combinaties van k unieke getallen in het interval
[1, n]. Bij invoer van n = 4 en k = 2 zou je programma als uitvoer [[2,4], [3,4], [2,3],
[1,2], [1,3], [1,4]] moeten teruggeven.
"""


def examine(n, k, partial_solution):
    if len(set(partial_solution)) == len(partial_solution) == k:
        return 'Accept'
    elif len(partial_solution) != len(set(partial_solution)):
        return 'Abandon'
    else:
        return 'Continue'


def extend(n, k, partial_solution):
    partial_solutions = []
    for i in range(1, n+1):
        if i not in partial_solution:
            partial_solutions.append(partial_solution + [i])
    return partial_solutions


def solve(n, k, partial_solution=[]):
    exam = examine(n, k, partial_solution)
    if exam == 'Accept':
        return [partial_solution]
    elif exam != 'Abandon':
        results = []
        for p in extend(n, k, partial_solution):
            if solve(n, k, p) is not None:
                for res in solve(n, k, p):
                    if sorted(res) not in results:
                        results.append(res)
        return results

print(solve(4,2))


