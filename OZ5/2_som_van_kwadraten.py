"""
Schrijf met behulp van een while lus een programma dat de som van de kwadraten van 1 t.e.m. n berekent.
Bewijs de correctheid.
"""
n = int(input('Geef n: '))

result = 0
i = 0
while i <= n:
    result += i**2
    i += 1
print(result)


