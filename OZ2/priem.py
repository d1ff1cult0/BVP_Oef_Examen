def is_prime():
    n = int(input('Geef een getal: '))
    delers = []
    for i in range(1, n+1):
        if n % i == 0 and i != n and i != 1:
            delers.append(i)
    if len(delers) != 0:
        print('Dit is geen priemgetal.')
        print(f'Delers: {delers}')
        return
    else:
        print('Dit is een priemgetal!')

is_prime()