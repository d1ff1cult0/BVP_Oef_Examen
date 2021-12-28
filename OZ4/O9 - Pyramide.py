"""
Schrijf een functie die een pyramide tekent als ze opgeroepen wordt. Deze functie
verwacht twee argumenten: als eerste de hoogte van de pyramide en als tweede een
optioneel argument dat het karakter meegeeft waarmee de pyramide getekend wordt.
Als er geen karakter wordt meegegeven bij oproep, wordt de pyramide getekend door
gebruik te maken van het + symbool.

Hint: De functie tekent de pyramide zelf en geeft geen resultaat terug.
Hint: Dit hoeft geen recursieve functie te zijn.
"""

def pyramide(n, char='+'):
    for i in range(1, n+1):
        print((n-i)*' ' + (i*2-1)*char)

pyramide(5, '*')
print('\n')
pyramide(7, '+')

