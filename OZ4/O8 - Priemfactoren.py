"""
Schrijf een recursieve functie factoren die de ontbinding in priemfactoren van een
positief geheel getal berekent. Vermijd het gebruik van lussen.

Schrijf ook een main-functie waarin je je ontbindingsfunctie controleert op
correctheid door gebruik te maken van assert statements. Schrijf dus een main-functie
rond de aanwezige asserts en bedenk zelf nog twee andere.

Hint: Je kan lijsten concateneren door gebruik te maken van de + operator.
"""


def factoren(n, x=2):
    result = []
    if n < x:
        return []
    if n % x == 0:
        return [x] + factoren(n/x, 2)
    return factoren(n, x+1)

def main():
    print(factoren(12))
    assert factoren(12) == [2, 2, 3]
    print(factoren(49))
    assert factoren(49) == [7, 7]
    print(factoren(1))
    assert factoren(1) == []
    print(factoren(7))
    assert factoren(7) == [7]

main()
