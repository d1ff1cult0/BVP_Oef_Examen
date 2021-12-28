def tictactoe():
    line1 = '+--+--+--+'
    line2 = '|  |  |  |'
    for i in range(7):
        if i % 2 == 0:
            print(line1)
        else:
            print(line2)

tictactoe()