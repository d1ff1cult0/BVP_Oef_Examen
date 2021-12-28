def fibonacci(n):
    f1 = 1
    f2 = 1
    i = 0
    if n == 1:
        print(f1)
    while i < n:
        print(f1)
        getal = f1 + f2
        f1 = f2
        f2 = getal
        i += 1

#fibonacci(int(input('Geef n: ')))

def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_list():
    n = int(input('Geef n:'))
    for i in range(1, n+1):
        print(fib_recursive(i))

fib_list()
