"""
Schrijf een functie die als 
input een zin/meerdere 
zinnen krijgt en een set teruggeeft 
met alle woorden in de tekst. 
"""


# Deze functie verwijdert alle speciale tekens van de zin
def no_special(text):
    import re
    text = re.sub("[^a-zA-Z0-9 ]+", "", text)
    return text

def woorden_uit_zin():
    zin = str(input('Geef een zin: '))
    zin = no_special(zin)
    return set(zin.split())

print(woorden_uit_zin())
