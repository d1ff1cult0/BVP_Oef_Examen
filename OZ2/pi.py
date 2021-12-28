import random, math
def pi(n):
    in_cirkel = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = math.sqrt(x**2+y**2)
        if distance <= 1:
            in_cirkel += 1
    return (in_cirkel/n)*4

print(pi(100000000))