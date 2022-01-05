"""
Gegeven volgende twee algoritmes die x^n berekenen. Ga na wat hun tijdscomplexiteit is door hun
recursievergelijkingen op te stellen en op te lossen. Bij de tweede versie zijn er twee mogelijke recursieve
oproepen: hier zul je rekening mee moeten houden. Je kan bij deze versie beginnen met na te gaan hoe het algoritme
zich gedraagt als n gelijk is aan een macht van 2, en pas daarna proberen te veralgemenen naar eender welke waarde
van n. Denk goed na over wanneer welke recursieve oproep plaatsvindt en of je hieruit een patroon kan afleiden.
"""


def power_v1(x, n):
    if n == 0:
        return 1
    else:
        return x * power_v1(x, n - 1)
# Best case: O(1)
# Worst case: O(n)


def power_v2(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return power_v2(x * x, n / 2)
    else:
        return x * power_v2(x, n - 1)

# Best case: O(1)
# Worst case: O(log(n))
