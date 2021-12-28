def ggd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(a)

ggd(int(input('Geef a: ')), int(input('Geef b: ')))