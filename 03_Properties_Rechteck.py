class Rechteck:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def seite(self):
        return self._a, self._b

    @seite.setter
    def seite(self, seitenlaengen):
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


mein_rechteck.seite = (10, 10)
print("Der Umfang beträgt:", mein_rechteck.umfang(), "cm")
print("Der Flächeninhalt beträgt:", mein_rechteck.flaecheninhalt(), "cm²")


mein_rechteck.seite = (-2, 0)
print("Der Umfang beträgt:", mein_rechteck.umfang(), "cm")
print("Der Flächeninhalt beträgt:", mein_rechteck.flaecheninhalt(), "cm²")

