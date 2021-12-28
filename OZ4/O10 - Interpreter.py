"""
Schrijf een functie interpret die eenvoudige  commando’s inleest en uitvoert.
Er zijn twee soorten commando’s:
    "add x y": tel x en y op, met x en y reële getallen.
    "subtract x y": trek y af van x, met x en y reële getallen.

De functie moet altijd een reëel getal teruggeven. Schrijf ook zelf een main-functie
waarin je je interpreter test door invoer op te vragen aan de gebruiker tot deze
"stop" ingeeft, samen met enkele assert statements.

Hint: Gebruik de split-functie om een string op te splitsen in verschillende delen.
"""

def interpreter():
    inp = str(input('Geef een commando: '))
    while inp != 'stop':
        inp = inp.split()
        if inp[0] == 'add':
            print(int(inp[1]) + int(inp[2]))
        if inp[0] == 'subtract':
            print(int(inp[1]) - int(inp[2]))
        if inp[0] != 'add' and inp[0] != 'subtract':
            print(f"'{inp[0]}' is geen geldig commando, probeer opnieuw.")
        inp = str(input('Geef een commando: '))
    return

interpreter()