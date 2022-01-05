"""
 In een bevraging moeten voetbalfans hun 3 
 favoriete voetbalteams kiezen (volgorde speelt geen rol). 
 De mogelijkheden zijn: "Bel", "Eng",“Ger", “Fra", 
 “Ita", “Spa" and “Cam". De resultaten zijn opgeslagen 
 in het bestand survey.txt. Zoek het antwoord op de 
 volgende vragen:
1. print de teams die door geen enkele fan gekozen zijn.
2. print het totaal aantal fans van wie zowel "Bel" als "
   Ger" een favoriet is.
3. maak een dictionary waarin je kan opzoeken 
   hoeveel fans voor elke combinatie van drie 
   teams hebben gekozen.
Hint: Je kan de volgende code gebruiken voor het lezen van informatie uit het bestand:
file=open("survey.txt","r") #hiermee open je het bestand enkel om het te lezen
for line in file.readlines(): # hiermee lees je het bestand lijn per lijn
	line=line.strip() # hiermee verwijder je het newline character	
	#hier kan je de lijn gebruiken in een functie
file.close() # sluit de file
"""

file = open("survey.txt", "r")
array = []
for line in file.readlines():
    line = line.strip()
    array.append(line)

def task1():
    gekozen = set()
    for i in range(len(array)):
        for j in array[i].split():
            gekozen.add(j)
    return {"Bel", "Spa", "Eng", "Ger", "Fra", "Ita", "Cam"} - gekozen

def task2():
    fan_van_b_en_g = 0
    for i in range(len(array)):
        if 'Bel' in array[i].split() and 'Ger' in array[i].split():
            fan_van_b_en_g += 1
    return fan_van_b_en_g

def task3():
    dict_teams = {}
    for i in array:
        if i not in dict_teams:
            dict_teams[i] = 1
        else:
            dict_teams[i] += 1
    return dict_teams

print(task1())
print(task2())
print(task3())