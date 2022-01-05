"""
Meestal zullen jullie berekenen of een getal even of oneven is door gebruik te maken van de modulo operator (n % 2
== 0).  We kunnen dit echter ook nagaan door gebruik te maken van volgende recursieve functies. Bereken hun
tijdscomplexiteit en ga na of deze efficiënter werken dan de beknopte modulo-vergelijking.
"""


def even(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return odd(n - 1)


def odd(n):
    if n == 1:
        return True
    elif n == 0:
        return False
    else:
        return even(n - 1)

# Best case: O(1)
# Worst case: O(n)
