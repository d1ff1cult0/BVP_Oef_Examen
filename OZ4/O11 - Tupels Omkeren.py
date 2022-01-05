"""
De functie reverse_tuple zou een tupel moeten teruggeven dat dezelfde elementen
bevat als de invoertupel, maar dan in omgekeerde volgorde. De code bevat vier
fouten, aan jou om deze te vinden en te corrigeren.
"""


def reverse_tuple(tuple):
    return tuple[::-1]


assert reverse_tuple(()) == ()
assert reverse_tuple((4,)) == (4,)
assert reverse_tuple((4, 6)) == (6, 4)
