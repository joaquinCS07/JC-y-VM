class Sede:
    def __init__(self, nombre, direccion, aforo_maximo):
        self.nombre= nombre
        self.direccion= direccion
        self.aforo_maximo= aforo_maximo

    def __str__(self):
        return f"Sede: {self.nombre} | Aforo: {self.aforo_maximo} personas"