"""
Volgende code onderzoekt of er twee elementen in een gesorteerde lijst bestaan zodat tussen hen het verschil
gelijk is aan delta. Met andere woorden, in dat geval geldt dat lst[i] - lst[j] = delta. Deze elementen
hoeven elkaar niet rechtstreeks op te volgen. Bereken de tijdscomplexiteit van het algoritme.
"""


def contains_delta(lst, delta):
    j = 0
    for i in range(0, len(lst)):
        while (j < len(lst) - 1) and (lst[i] - lst[j] > delta):
            j = j + 1
        if lst[i] - lst[j] == delta:
            return True
    return False

# Worst case: O(n)
# Best case: O(1)
