def quadruplets(r1, r2):
    r2 += 1
    solutions = []
    for a in range(r1, r2):
        for b in range(r1, r2):
            for c in range(r1, r2):
                for d in range(r1, r2):
                    if a**3+b**3 == c**3+d**3:
                        if a != c and b != d:
                            if a != d and b != c:
                                same_solution = 0
                                for i in solutions:
                                    if set(i) == {a, b, c, d}:
                                        same_solution += 1
                                if same_solution == 0:
                                    solutions.append([a, b, c, d])
    print(solutions)

quadruplets(1, 15)