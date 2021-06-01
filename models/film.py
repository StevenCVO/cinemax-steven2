class Film():

    def __init__(self, titel, duur):
        self.titel = titel
        self._duur = duur

    @property
    def duur(self):
        return self._duur

    @duur.setter
    def duur(self, waarde):
        try:
            self._duur = int(waarde)
        except ValueError:
            raise