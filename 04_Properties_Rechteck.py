# 1

class Rechteck:
    def __init__(self, a, b):
        self._a = None
        self._b = None
        self.a = a
        self.b = b
        
    @property
    def a(self):
        return self._a
        
    @a.setter
    def a(self, value):
        if value <= 0:
            raise ValueError("Seitenlänge a muss größer als 0 sein.")
        self._a = value

    @property
    def b(self):
        return self._b
        
    @b.setter
    def b(self, value):
        if value <= 0:
            raise ValueError("Seitenlänge b muss größer als 0 sein.")
        self._b = value
    
    @property
    def umfang(self):
        return 2 * (self.a + self.b)
        
    @property
    def flaeche(self):
        return self.a * self.b

# 3 
    def __eq__(self, other):
            if isinstance(other, Rechteck):
                return self.a == other.a and self.b == other.b
            return False
        
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __lt__(self, other):
        if isinstance(other, Rechteck):
            return self.flaeche < other.flaeche
        return NotImplemented
        
    def __le__(self, other):
        if isinstance(other, Rechteck):
            return self.flaeche <= other.flaeche
        return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, Rechteck):
            return self.flaeche > other.flaeche
        return NotImplemented
        
    def __ge__(self, other):
        if isinstance(other, Rechteck):
            return self.flaeche >= other.flaeche
        return NotImplemented
        
    def __str__(self):
        return f"Rechteck: Seitenlängen({self.a}, {self.b}), Umfang({self.umfang}), Flächeninhalt({self.flaeche})"
        
    def __repr__(self):
        return f"Rechteck({self.a}, {self.b})"

try:
    r = Rechteck(1, 6)
    print(f"Umfang:{r.umfang}cm²")
    print(f"Fläche:{r.flaeche}cm²")
except ValueError as e:
     print(e)

# 2

class AsciiRechteck(Rechteck):
    def __init__(self, a, b, zeichen):
        super().__init__(a, b)
        self._zeichen = None
        self.zeichen = zeichen

    @property
    def zeichen(self):
        return self._zeichen
    
    @zeichen.setter
    def zeichen(self, value):
        if len(value) != 1:
            print("Das Zeichen muss genau ein Zeichen lang sein")
        self._zeichen = value

    def zeichnen(self):
        for _ in range(self.a):
            print(self.zeichen * self.b)

ascii_rect = AsciiRechteck(5, 3, "*")
ascii_rect.zeichnen()
