"""
Gegeven volgende code voor het berekenen van de zadelpunten van een matrix m. Je mag ervan uitgaan dat de dimensie
van deze matrix gelijk is aan n * n. Bereken de tijdscomplexiteit van de functie get_saddle_points in functie van
deze n^2.

Deze functie maakt gebruik van de functie is_saddle. Je zal dus ook voor is_saddle moeten nagaan wat de
tijdscomplexiteit is. Hieronder vind je ook een functie main, waarvan je de tijdscomplexiteit niet hoeft te
berekenen. Je kan deze functie echter wel gebruiken om de code uit te voeren.
"""


def is_saddle(m, x, y):
    if (m[x][y] > m[x - 1][y] and m[x][y] > m[x + 1][y] and
        m[x][y] < m[x][y + 1] and m[x][y] < m[x][y - 1]
    ) or (
            m[x][y] < m[x - 1][y] and m[x][y] < m[x + 1][y] and
            m[x][y] > m[x][y + 1] and m[x][y] > m[x][y - 1]):
        return True
    else:
        return False


def get_saddle_points(m):
    saddles = []

    for i in range(1, len(m) - 1):
        for j in range(1, len(m[i]) - 1):
            if is_saddle(m, i, j):
                saddles.append((i, j))

    return saddles
# Best en worst case: O(n^2)


def main():
    m = [
        [1, 2, 3, 4, 5],
        [5, 3, 0, 1, 0],
        [6, 4, 2, 7, 8],
        [5, 7, 5, 4, 2],
        [4, 5, 1, 9, 1]
    ]

    saddle_points = get_saddle_points(m)

    for sdl in saddle_points:
        print(sdl)


main()
