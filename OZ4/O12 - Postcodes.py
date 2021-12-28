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
