"""
Schrijf met behulp van een while lus een programma dat n! berekent.
Bewijs de correctheid.
"""
import math
def fac(n):
    assert n >= 0 and type(n) == int
    i = 1
    result = 1
    assert result == math.factorial(i)
    while i <= n:
        result *= i
        i += 1
        assert result == math.factorial(i)
    assert result == math.factorial(n)
    return result

print(fac(0))