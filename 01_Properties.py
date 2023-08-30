class Speaker():
    def __init__(self, v):
        self.__volume = v

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, v):
        if 0 <= v <= 100:
            self.__volume = v

mein_lautsprechner = Speaker(50)
print(mein_lautsprechner.volume)
mein_lautsprechner.volume = 75
print(mein_lautsprechner.volume)
mein_lautsprechner.volume = 150
print(mein_lautsprechner.volume)