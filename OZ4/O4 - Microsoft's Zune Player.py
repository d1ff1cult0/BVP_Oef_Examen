"""
De code berekent het jaartal gegeven het aantal dagen die men kan tellen sinds het
begin van 1980. Zo komt 1 januari 1980 komt overeen met dag 1. Als je 367 ingeeft,
moet het resultaat 1981 zijn. Het is dan immers 1 januari 1981. Voor 366 moet het
resultaat 1980 zijn. Wanneer je echter 366 invoert, komt het programma in een
oneindige lus terecht: enkele statements worden steeds opnieuw uitgevoerd en het
programma zal nooit eindigen. Verifiëer met de debugger om welke lijnen code het gaat.
"""

from calendar import isleap

ORIGIN_YEAR = 1980
days = int(input('Days since 1st January ' + str(ORIGIN_YEAR) + "? "))

year = ORIGIN_YEAR
while days > 365:
    if isleap(year):
        if days >= 366:
            days -= 366
            year += 1
    else:
        days -= 365
        year += 1

print('The current year is', year)
