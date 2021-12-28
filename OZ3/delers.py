def delers():
    n = int(input('Geef een getal: '))
    delers = []
    for i in range(1, n+1):
        if n % i == 0:
            delers.append(i)
    print(delers)

delers()