def lijsten_vergelijken(lijst1, lijst2):
    gemeenschappelijk = 0
    len_lijst = len(lijst1)
    if len_lijst != len(lijst2):
        return False
    for i in sorted(lijst1):
        for j in sorted(lijst2):
            if i == j:
                gemeenschappelijk += 1
                lijst1.remove(i)
                lijst2.remove(j)
    if gemeenschappelijk == len_lijst:
        return True
    else:
        return False

print(lijsten_vergelijken([1, 3, 9, 6, 4, 3, 12, 11, 98], [98, 6, 4, 1, 3, 9, 12, 11, 3]))

def lijsten_vergelijken2(lijst1, lijst2):
    if len(lijst1) != len(lijst2):
        return False
    i = 0
    same = 0
    lijst1.sort()
    lijst2.sort()
    while i < len(lijst1):
        if lijst1[i] == lijst2[i]:
            same += 1
        i += 1
    if same == len(lijst1):
        return True
    else:
        return False

print(lijsten_vergelijken2([1, 3, 9, 6, 4, 3, 12, 11, 98], [98, 6, 4, 1, 3, 9, 12, 11, 3]))