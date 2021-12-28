def lijst_inlezen():
    lijst = []
    for i in range(10):
        getal = int(input('Geef een positief geheel getal: '))
        while getal < 0:
            getal = int(input('Getallen moeten positief zijn, geef een nieuw getal: '))
        lijst.append(getal)
    print(lijst)

lijst_inlezen()