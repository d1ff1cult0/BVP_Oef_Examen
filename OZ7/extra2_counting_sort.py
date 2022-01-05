"""
Counting sort is een zeer efficiënt sorteer algoritme, indien
alle getallen in de lijst groter dan 0 en kleiner dan n (waarbij
n gegeven is). Het algoritme werkt in 3 stappen (de gegeven
voorbeelden zijn voor de lijst [1, 4, 1, 2, 7, 5, 2]):

 1. Initialiseer een nieuwe lijst aantal van lengte n+1 en itereer
    over de gegeven lijst zodat op index i het aantal voorkomens
    van getal i staat.
    aantal: [0, 2, 2, 0, 1, 1, 0, 1, 0, 0]

 2. Pas de aantal lijst aan zodat elk element de som is van de
    vorige aantallen.
    aantal: [0, 2, 4, 4, 5, 6, 6, 7, 7, 7]
    Deze lijst stelt de positie van elk element voor in de
    gesorteerde lijst.

 3. De aantal lijst zegt nu op welke index ieder getal in de
    gesorteerde lijst moet voorkomen. Itereer over de getallen in
    de originele lijst en voeg deze op de correct positie toe in
    de gesorteerde lijst. Zorg ervoor dat je de waarde in de
    aantal lijst met 1 verlaagt wanneer je een getal toevoegt.

Schrijf een functie die de een lijst sorteer met behulp van Counting
Sort. Geef n mee als een parameter van de functie.

Waarom moet je n kennen in dit algoritme? Zou dit algoritme ook
werken om komma getallen te sorteren? En negatieve getallen?
"""

def counting_sort(lijst, n):
    aantal = [0]*(n+1)
    for i in lijst:
        aantal[i] += 1
    indices = [0] * (n+1)
    indices[0] = aantal[0] - 1
    for i in range(1, n + 1):
        indices[i] = indices[i - 1] + aantal[i]
    sorted_list = [0]*len(lijst)
    for i in lijst:
        sorted_list[indices[i]] = i
        indices[i] -= 1
    return sorted_list


print(counting_sort([1, 4, 1, 2, 7, 5, 2], 10))
assert(counting_sort([1, 4, 1, 2, 7, 5, 2], 10) == [1, 1, 2, 2, 4, 5, 7])