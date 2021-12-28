def alternating_sum(lijst):
    som = 0
    for i in range(len(lijst)):
        if i % 2 == 0:
            som += lijst[i]
        else:
            som -= lijst[i]
    return som

print(alternating_sum([1, 4, 9, 16, 9, 7, 4, 9, 11]))