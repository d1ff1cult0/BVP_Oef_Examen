"""
Binary Search zoekt door een gesorteerde lijst in twee te splitsen en
vervolgens in slechts één helft verder te zoeken. Het Ternary Search
algoritme werkt analoog, maar zal de gesorteerde lijst in drie gelijke
delen splitsen. Implementeer een zoek algoritme om de index van een
gegeven waarde in een gesorteerde lijst te zoeken, gebruik makende van
het Ternary Search algoritme. Indien het element niet in de lijst
voorkomt, dan moet het algoritme -1 terug geven.
"""
import math


def ternary_search(x, lijst, l=0, r=0):
    if r == 0:
        r = len(lijst)-1
    if r >= l:
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3
        if lijst[mid1] == x:
            return mid1
        if lijst[mid2] == x:
            return mid2
        if x < lijst[mid1]:
            return ternary_search(x, lijst, l, mid1-1)
        if lijst[mid1] < x < lijst[mid2]:
            return ternary_search(x, lijst, mid1+1, mid2-1)
        if x > lijst[mid2]:
            return ternary_search(x, lijst, mid2+1, r)
    return -1

# Tests om te kijken of de implementatie correct is
assert ternary_search(8, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 4
assert ternary_search(5, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 2
assert ternary_search(17, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 8
assert ternary_search(12, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == -1
