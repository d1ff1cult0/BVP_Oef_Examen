def reformat(getal):
    reformatted = ''
    for i in range(len(str(getal))):
        if i%3 != 0 or i == 0:
            reformatted += str(getal)[i]
        else:
            reformatted += ' ' + str(getal)[i]
    return reformatted

print(reformat(642013))