class Konto:
    def __init__(self, gk, tg):
        self.girokonto = gk
        self.tagesgeld = tg

    @property
    def kontostand(self):
        return self.girokonto + self.tagesgeld

mein_konto = Konto(800, 50)
print(mein_konto.kontosand)