class Tovar:
    def __init__(self, id, nazvanie,  price, nalichie, ves):
        self.id = id
        self.nazvanie = nazvanie
        self.price = price
        self.nalichie = nalichie
        self.ves = ves

    def __str__(self):
        return f"{self.id} {self.nazvanie} {self.price} {self.nalichie} {self.ves}"