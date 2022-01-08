"""

    Klass die een robot voorstelt, elke robot heeft een identiteit die als nummer wordt voorgesteld.

"""


class Robot:
    # constructor van de robot klas. Deze heeft als parameter zijn identiteits nummer.
    def __init__(self, nummer):
        self.number = nummer

    # Deze methode moet een groet printen met het nummer van de robot erin
    def say_hello(self):
        print(f'Hallo robot {self.number}')


"""

    Klass Legioen. Stelt een legioen van robots voort.

"""


class Legion:
    # Constructor van een legioen. Hier moet er een verzameling van robots gemaakt worden die in het begin leeg is.
    def __init__(self):
        self.robots_verzameling = set()

    # Voeg een nieuwe robot toe aan de Legioen.
    def add_robot(self, robot):
        self.robots_verzameling.add(robot)

    # Zorg ervoor dat elke robot die deel maakt van dit legioen zich presenteert.
    def present(self):
        for i in self.robots_verzameling:
            i.say_hello()



l = Legion()
# Add robots that are identified by a number.
l.add_robot(Robot(2468))
l.add_robot(Robot(1357))
l.add_robot(Robot(2580))
# Add robots that are identified by a name.
l.add_robot(Robot("R2D2"))
l.add_robot(Robot("C3PO"))
l.present()
