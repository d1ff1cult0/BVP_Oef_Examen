"""
Gegeven een dictionary met als keys producten die je kan kopen in een supermarkt en als
bijbehorende waarden hun prijzen. Schrijf een functie die door middel van backtracking berekent
wat er in de supermarkt gekocht kan worden, rekening houdende met het volgende:
    1. Enkel de producten in de gegeven dictionary zijn te koop in de winkel.
    2. Je functie krijgt ook als argument een lijst mee met verboden producten, deze zijn al dan
    niet te koop in de winkel en mogen niet in je resultaat zitten.
    3. Je functie krijgt ook een maximumbedrag mee, je mag niet voor meer geld kopen dan dit
    budget.
    4. Je mag meerdere keren hetzelfde item kopen, zolang dat binnen je budget past.
    5. Als je nog budget overhebt om een product toe te voegen aan je winkellijstje, moet je dat
    ook doen. Het lijstje is pas compleet als er geen extra product meer aan toegevoegd kan
    worden.
    6. Het resultaat van je functie is een lijst met winkellijstjes, waarop staat wat er gekocht kan
    worden voor het gegeven budget en rekening houdende met de verboden producten.
"""


# De argumenten zijn reeds meegegeven bij de solve-functie om je op weg te zetten. Kies zelf nog wat je verwacht bij
# examine en extend! Hulpfuncties definiëren kan ook nuttig zijn.

def examine():
    pass


def extend():
    pass


def solve(producten, verboden_producten, bedrag, lijstje=None):
    # Het lijstje zal je boodschappenlijstje voorstellen - dit is je (partiële) oplossing.
    # Om te vermijden dat Python onze lege lijst, die we als standaardwaarde mee zouden geven, opnieuw zou gebruiken
    # bij het heroproepen van de functie, kunnen we als standaardwaarde ook 'None' meegeven en deze veranderen in de
    # lege lijst in het lichaam van de functie zelf. Zo hebben we geen last van Pythons referentiesemantiek!
    if lijstje == None:
        lijstje = []  # De lege lijst die we hier aanmaken blijft enkel beschikbaar binnen déze oproep van de functie
    pass


# Voorbeeld dictionary met koopwaar en prijzen
koopwaar = {'Bloemkool': 4, 'Pompoen': 3, 'Koekjes': 2, 'Champignons': 5, 'Champagne': 10}

print(solve(koopwaar, ['Koekjes', 'Bloemkool', 'Chips'], 10))  # Voorbeeld-oproep
