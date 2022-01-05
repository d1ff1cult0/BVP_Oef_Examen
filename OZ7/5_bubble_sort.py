"""
Bubble Sort is een sorteer algoritme dat aangrenzende waarden
in een lijst vergelijkt, en indien nodig wisselt van plaats.
Schrijf een functie die het Bubble Sort algoritme gebruikt om
een lijst te sorteren.
"""

def bubble_sort(lijst):
    swapped = 1
    while swapped > 0:
        swapped = 0
        for i in range(len(lijst)-1):
            if lijst[i] > lijst[i+1]:
                lijst[i], lijst[i+1] = lijst[i+1], lijst[i]
                swapped += 1
    return lijst


assert(bubble_sort([20, 18, 10, 6, 15, 3, 9, 7, 11, 20, 9, 5, 12, 8, 17]) == [3, 5, 6, 7, 8, 9, 9, 10, 11, 12, 15, 17, 18, 20, 20])
print(bubble_sort([20, 18, 10, 6, 15, 3, 9, 7, 11, 20, 9, 5, 12, 8, 17]))