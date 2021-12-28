def inwendig_product():
    tup1 = input('Geef vector u: ')
    tup1 = tuple(int(x) for x in tup1.split(","))
    tup2 = input('Geef vector v: ')
    tup2 = tuple(int(x) for x in tup2.split(","))
    return tup1[0]*tup2[0] + tup1[1]*tup2[1]


print(inwendig_product())
