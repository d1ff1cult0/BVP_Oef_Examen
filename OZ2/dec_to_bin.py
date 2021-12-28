import math
def decimaal_naar_binair(number):
    bitstring = ''
    while number > 0:
        bit = str(number%2)
        quotient = math.floor(number/2)
        bitstring = bit + bitstring
        number = quotient
    print(bitstring)
    bitstring = '0b' + bitstring
    print(bitstring)

decimaal_naar_binair(int(input('Geef een getal: ')))
