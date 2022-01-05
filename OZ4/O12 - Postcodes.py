"""
In de USA worden postcodes geschreven in barcodes. Elke postcode bevat vijf cijfers
en een controlecijfer, dat op een specifieke manier berekend wordt. Eerst worden de
vijf cijfers van de postcode opgeteld. Het controlecijfer is dan het cijfer dat je
bij deze som nog zou moeten optellen om tot een veelvoud van 10 te komen. Zo
sommeert de postcode 95104 bijvoorbeeld tot 19 en heeft deze als controlecijfer 1.

CONTROLECIJFER
Schrijf een functie die, gegeven een postcode, het controlecijfer berekent en
teruggeeft. Je functie maakt gebruik van hulpfuncties om het werk overzichtelijker
te houden.

BARCODE
Cijfers kunnen tot een barcode omgevormd worden door gebruik te maken van de tekens
| en :. Schrijf een functie die één cijfer omzet naar een string die de barcode
bevat op basis van de tabel op het opgaveblad.

OMZETTING
Schrijf tenslotte een functie die gebruik maakt van de eerder besproken functies
om alles samen te brengen. Deze functie krijgt als argument een postcode en
genereert een barcode voor de vijf cijfers én voor het controlecijfer. Tussen de
barcodes van de verschillende cijfers staat steeds een spatie.
"""


def controlecijfer(postcode):
    som = 0
    for digit in str(postcode):
        som += int(digit)
    return 10 - int(str(som)[-1])


def cijfer_naar_barcode(cijfer):
    if cijfer == 1:
        return ':::||'
    if cijfer == 2:
        return '::|:|'
    if cijfer == 3:
        return '::||:'
    if cijfer == 4:
        return ':|::|'
    if cijfer == 5:
        return ':|:|:'
    if cijfer == 6:
        return ':||::'
    if cijfer == 7:
        return '|:::|'
    if cijfer == 8:
        return '|::|:'
    if cijfer == 9:
        return '|:|::'
    if cijfer == 0:
        return '||:::'


def postcode_naar_bar(postcode):
    string1 = ''
    for i in str(postcode):
        string1 += f' {cijfer_naar_barcode(int(i))}'
    string1 += f' {cijfer_naar_barcode(controlecijfer(postcode))}'
    return string1[1:]  # deletes first space from string


print(controlecijfer(82103))
print(postcode_naar_bar(82103))
