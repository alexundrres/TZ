class Punkt:
    def __init__(self, id_client, id_tovar, id_zakaz, id_check):
        self.id_client = id_client
        self.id_tovar = id_tovar
        self.id_zakaz = id_zakaz
        self.id_check = id_check

    def __str__(self):
        return f"{self.id_client} {self.id_tovar} {self.id_zakaz} {self.id_check}"