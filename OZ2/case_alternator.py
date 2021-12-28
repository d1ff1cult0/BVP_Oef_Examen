def case_alternator():
    str1 = str(input('Geef een string: '))
    str2 = ''
    for i in range(len(str1)):
        if i % 2 == 0:
            str2 += f'{str1[i].upper()}'
        else:
            str2 += f'{str1[i].lower()}'
    print(str2)

case_alternator()