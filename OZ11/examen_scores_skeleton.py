class ScoreBlad:
    def __init__(self, naam):
        self.naam_student = naam
        self.vakken = {}

    def naam_van_student(self):
        return self.naam_student

    def registreer_vak(self, vak):
        if vak not in self.vakken.keys():
            self.vakken[vak] = []

    def voeg_score_toe_voor(self, vak, score):
        if vak not in self.vakken.keys():
            self.registreer_vak(vak)
        if score == "NA":
            self.vakken[vak].append(0)
        else:
            self.vakken[vak].append(score)

    def resultaten_voor(self, vak):
        if vak not in self.vakken.keys():
            return None
        else:
            return self.vakken[vak]

    def alle_vakken(self):
        return self.vakken.keys()

    def hoogste_score_voor(self, vak):
        if vak not in self.vakken.keys():
            return None
        if len(self.vakken[vak]) == 0:
            return None
        else:
            return max(self.vakken[vak])

    def gemiddelde_score(self):
        scores = []
        for vak in self.alle_vakken():
            scores.append(self.hoogste_score_voor(vak))
        if not scores:
            return None
        else:
            return round(sum(scores) / len(scores))

    def aantal_pogingen_voor_gefaalde_vakken(self):
        gefaald = []
        for vak in self.vakken:
            if self.hoogste_score_voor(vak) < 10:
                gefaald.append((vak, len(self.resultaten_voor(vak))))
        return frozenset(gefaald)


# TESTS

resultaten = ScoreBlad("Jan")
assert resultaten.naam_van_student() == "Jan"
resultaten.registreer_vak("Methodiek van de informatica")
assert resultaten.alle_vakken() == {"Methodiek van de informatica"}
assert resultaten.resultaten_voor("Methodiek van de informatica") == []

resultaten.voeg_score_toe_voor("Methodiek van de informatica", 16)
resultaten.voeg_score_toe_voor("Methodiek van de informatica", 14)
resultaten.voeg_score_toe_voor("Toegepaste Mechanica", 10)
assert resultaten.resultaten_voor("Methodiek van de informatica") == [16, 14]
assert resultaten.resultaten_voor("Toegepaste Mechanica") == [10]
assert resultaten.alle_vakken() == {"Methodiek van de informatica", "Toegepaste Mechanica"}

# Een vak dat al geregistreerd is opnieuw toevoegen veranderd niks aan de huidige scores.
resultaten.registreer_vak("Methodiek van de informatica")
assert resultaten.resultaten_voor("Methodiek van de informatica") != []

resultaten.voeg_score_toe_voor("Analyse 2", "NA")
assert resultaten.hoogste_score_voor("Methodiek van de informatica") == 16
assert resultaten.hoogste_score_voor("Analyse 1") is None
assert resultaten.hoogste_score_voor("Analyse 2") == 0
assert resultaten.gemiddelde_score() == 9  # NA wordt als 0 gerekend.
assert resultaten.aantal_pogingen_voor_gefaalde_vakken() == frozenset([("Analyse 2", 1)])
print("OK!")
