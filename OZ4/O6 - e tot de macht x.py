"""
Vind de drie fouten in onderstaande implementatie.
Bij een correcte implementatie krijg je bijv. volgende resultaten:

x = 2
n = 20
resultaat = 7.389056

---

x = 5
n = 5
resultaat = 91.416667

---

x = 5
n = 20
resultaat = 148.413147

"""

import math


def fac(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac



def estimate_exp(x, n):
    som = 0
    for i in range(0, n+1):
        term = x**i / fac(i)
        som += term
    return som


def main():
    x = int(input("Enter x: "))
    n = int(input("Enter n: "))
    print("e powered by %d is %f" % (x, estimate_exp(x, n)))


main()
