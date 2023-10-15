class Check:
    def __init__(self, id, id_tovar, kolich_tov, summa):
        self.id = id
        self.id_tovar = id_tovar
        self.kolich_tov = kolich_tov
        self.summa = summa

    def __str__(self):
        return f"{self.id} {self.id_tovar} {self.kolich_tov} {self.summa}"