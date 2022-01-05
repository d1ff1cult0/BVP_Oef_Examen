"""
Schrijf drie functies die als input twee 
strings heeft en als output respectievelijk:
1) een set met alle hoofdletters en kleine 
   letters die in beide strings zitten
2) een set met alle hoofdletters en kleine 
   letters die in geen van beide strings zitten
3) een set met alle niet-letter tekens 
   die in beide strings zitten
"""
string1 = 'Bonjour je suis ne kloot'
string2 = 'Bananen zijn lekker'
string3 = 'B.on/joué#r banân$enùzijn;lekke§r'
string4 = '#je@suis §ène àkloot$'

def task1(str1, str2):
    set_letters = set()
    for i in str1:
        if i in str2 and i != ' ':
            set_letters.add(i)
    return sorted(set_letters)

def task2(str1, str2):
    alfabet = 'abcdefghijklmnopqrtsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return sorted(set(alfabet)-set(str1)-set(str2))

def task3(str1, str2):
    beide = task1(str1, str2)
    alfabet = 'abcdefghijklmnopqrtsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for i in beide:
        if i not in alfabet:
            result.append(i)
    return sorted(result)




print(task1(string1, string2))
print(task2(string1, string2))
print(task3(string3, string4))