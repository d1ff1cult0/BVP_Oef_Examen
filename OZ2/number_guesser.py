import random

def number_guesser():
    number = random.randrange(20)
    guessed = int(input('Gok een getal tussen 0 en 20: '))
    while guessed != -1 and guessed != number:
        guessed = int(input('Fout! Gok een getal tussen 0 en 20: '))
    if guessed == number:
        print('Correct!')
    else:
        return


number_guesser()
