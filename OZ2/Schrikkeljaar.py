def schrikkeljaar(jaar):
    if jaar % 4 == 0 and (jaar % 100 != 0 or (jaar % 100 == 0 and jaar % 400 == 0)):
        return True
    else:
        return False


print(schrikkeljaar(int(input('Geef jaar: '))))
