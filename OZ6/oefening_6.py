"""
 Schrijf een programma dat een set teruggeeft van 
 alle elementen die in beide sets voorkomen.
"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

def samen_in_set(s1, s2):
    return s1.intersection(s2)

print(samen_in_set(set1, set2))