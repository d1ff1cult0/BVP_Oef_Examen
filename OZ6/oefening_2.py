"""
Schrijf een programma dat als input een getal tussen 1 en 10 krijgt en als output dit getal voluit schrijft. Gebruik hiervoor een dictionary.
"""
def getal_voluit(getal):
    dict1 = {0: 'Nul', 1: 'één', 2: 'Twee', 3: 'Drie', 4: 'Vier', 5: 'Vijf', 6: 'Zes', 7: 'Zeven', 8: 'Acht',
             9: 'Negen', 10: 'Tien'}
    return dict1[getal]

print(getal_voluit(0))

