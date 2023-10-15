from Tovari import Tovar
from Punkt_ofor import Punkt
from Check import Check
from Zakaz import Zakaz


class Clients:
    def __init__(self, id, fio, contdan):
        self.id = id
        self.fio = fio
        self.contdan = contdan
        self.things = []

    def __str__(self):
        return f"{self.id} {self.fio} {self.contdan} {self.things}"


with open("clients.txt", encoding="UTF-8") as clients_file:
    line = clients_file.readline()
    id, fio, contdan = line.split(";")
    id = int(id)
    fio = str(fio)
    contdan = str(contdan)
    clients = Clients(id, fio, contdan)


with open("tovar.txt", encoding="UTF-8") as tovar_file:
    line = tovar_file.readline()
    id, nazvanie, price, nalichie, ves = line.split(";")
    id = int(id)
    nazvanie = str(nazvanie)
    price = float(price)
    nalichie = str(nalichie)
    ves = float(ves)
    tovar = Tovar(id, nazvanie, price, nalichie, ves)


for things in Clients.things:
    print(str(things), end='; ')