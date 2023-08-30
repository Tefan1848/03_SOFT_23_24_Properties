class Rechteck:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def seiten(self):
        return self._a, self._b

    @seiten.setter
    def seiten(self, seitenlaengen):
        a, b = seitenlaengen
        if a <= 0 or b <= 0:
            print("Die Seitenlänge muss größer als 0 sein!")
        else:
            self._a = a
            self._b = b

    def umfang(self):
        return 2 * (self._a + self._b)

    def flaecheninhalt(self):
        return self._a * self._b

mein_rechteck = Rechteck(5, 5)
print("Der Umfang beträgt:", mein_rechteck.umfang(), "cm")
print("Der Flächeninhalt beträgt:", mein_rechteck.flaecheninhalt(), "cm²")


mein_rechteck.seiten = (10, 10)
print("Der Umfang beträgt:", mein_rechteck.umfang(), "cm")
print("Der Flächeninhalt beträgt:", mein_rechteck.flaecheninhalt(), "cm²")


mein_rechteck.seiten = (-2, 0)
print("Der Umfang beträgt:", mein_rechteck.umfang(), "cm")
print("Der Flächeninhalt beträgt:", mein_rechteck.flaecheninhalt(), "cm²")

class AsciiRechteck(Rechteck):

    def __init__(self, a, b, zeichen):
        super().__init__(a, b)
        self._zeichen = zeichen

    @property
    def zeichen(self):
        return self._zeichen

    @zeichen.setter
    def zeichen(self, zeichen):
        if len(zeichen) == 1:
            self._zeichen = zeichen
        else:
            print("Das Zeichen muss genau ein Zeichen lang sein!")

    def zeichne(self):
        for i in range(self._b):
            print(self._zeichen * self._a)

mein_ascii_rechteck = AsciiRechteck(5, 5, ")")
mein_ascii_rechteck.zeichne()

