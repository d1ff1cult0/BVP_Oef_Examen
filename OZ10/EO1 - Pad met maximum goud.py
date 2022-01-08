doolhof = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]

def examine(maze, partial_solution):
    met_goud = 0
    for i in partial_solution:
        if maze[i[0]][i[1]] > 0:
            met_goud += 1
    if len(set(partial_solution)) == len(partial_solution) == met_goud > 0 and accept(maze, partial_solution):
        return 'Accept'
    if len(partial_solution) != 0 and (met_goud != len(partial_solution) or partial_solution[-1] in partial_solution[:-1]):
        return 'Abandon'
    else:
        return 'Continue'

def accept(maze, partial_solution):
    x1 = partial_solution[-1][0]
    y1 = partial_solution[-1][1]
    possible_positions = [[x1 - 1, y1], [x1, y1 - 1], [x1 + 1, y1], [x1, y1 + 1]]
    niet_mogelijk = 0
    for i in possible_positions:
        if i[0] < 0 or i[0] > len(maze):
            niet_mogelijk += 1
        elif i[1] < 0 or i[1] > len(maze[0]):
            niet_mogelijk += 1
        elif i in partial_solution:
            niet_mogelijk += 1
    if niet_mogelijk == 4:
        return True
    else:
        return False





def extend(maze, partial_solution):
    solutions = []
    if len(partial_solution) != 0:
        x1 = partial_solution[-1][0]
        y1 = partial_solution[-1][1]
        if x1 != 0:
            if [(x1 - 1, y1)] not in partial_solution:
                solutions.append(partial_solution + [(x1 - 1, y1)])
        if y1 != 0:
            if [(x1, y1-1)] not in partial_solution:
                solutions.append(partial_solution + [(x1, y1 - 1)])
        if x1 != len(maze) - 1:
            if [(x1 + 1, y1)] not in partial_solution:
                solutions.append(partial_solution + [(x1 + 1, y1)])
        if y1 != len(maze[0]) - 1:
            if [(x1, y1+1)] not in partial_solution:
                solutions.append(partial_solution + [(x1, y1 + 1)])
        #print(solutions)
        return solutions
    else:
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] != 0:
                    if [(i, j)] not in partial_solution:
                        solutions.append(partial_solution + [(i, j)])
        return solutions


def solve(maze, partial_solution= [], solutions=[]):
    exam = examine(maze, partial_solution)
    if exam == 'Accept':
        solutions.append(partial_solution)
    elif exam != 'Abandon':
        for p in extend(maze, partial_solution):
            solve(maze, p, solutions)
        return solutions
    return 0

def pad_met_meeste_goud(maze):
    pass

doolhof2 = [[1, 0, 7],
            [2, 0, 6],
            [3, 4, 5],
            [0, 3, 0],
            [9, 0, 20]]
print(solve(doolhof2))
print(pad_met_meeste_goud(doolhof2))

#print(solve(doolhof))