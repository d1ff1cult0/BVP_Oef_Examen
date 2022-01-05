"""
In cryptografie is caesar cipher een encryptietechniek
waarin elke letter in het alfabet vervangen wordt door
een letter die een aantal posities verder in het alfabet 
staat. In dit geval implementeren we ROT-13, waarbij elke 
letter dertien plaatsen opschuift. Een a zou bijvoorbeeld 
een n worden. Schrijf hiervoor een encoder en decoder en 
vertaal/codeer hiermee de volgende twee berichten:
Pnrfne pvcure? V zhpu cersre Pnrfne fnynq! 
Gebruik voor deze opgave een dictionary!
"""

def caesar_cipher(zin):
    dict = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
            'k': 'x', 'l': 'y', 'm': 'z',
            'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j',
            'x': 'k', 'y': 'l', 'z': 'm',
            ' ': ' ', '?': '?', '!': '!', '.': '.'}
    vertaalde_zin = ''
    for i in zin:
        if i == i.upper():
            vertaalde_zin += dict[i.lower()].upper()
        else:
            vertaalde_zin += dict[i.lower()]
    return vertaalde_zin

print(caesar_cipher('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))
