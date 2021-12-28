"""
Schrijf een functie die twee reeds gesorteerde sequenties omzet naar één gesorteerde
sequentie die alle elementen van de reeksen bevat, inclusief duplicaten. Als een
element bijvoorbeeld tweemaal voorkomt in de eerste reeks en driemaal in de tweede,
zal de resultaatreeks dit element vijf keer moeten bevatten.

Je mag geen gebruik maken van de ingebouwde sort-functie. Gebruik het gegeven dat de
twee originele reeksen reeds gesorteerd zijn om dit probleem zelf door middel van
recursie op te lossen.
"""
def sort_sequences(lijst1, lijst2):
    merged_list = lijst1+lijst2
    sorted_list = []
    while merged_list:
        minimum = merged_list[0]
        for i in merged_list:
            if i < minimum:
                minimum = i
        sorted_list.append(minimum)
        merged_list.remove(minimum)
    return sorted_list


list_a = [2, 3, 3, 6, 8, 11, 11, 12, 12, 12]
list_b = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 11, 12, 13]
print(sort_sequences(list_a, list_b))
