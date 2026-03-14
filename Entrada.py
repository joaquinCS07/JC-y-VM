class Entrada:
    def __init__(self, id_entrada, precio_base):
        self.id_entrada = id_entrada
        self.precio_base = precio_base

    def __str__(self):
        return f"Entrada #{self.id_entrada} | Precio: {self.precio_base}€"



