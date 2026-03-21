class Sede:
    def __init__(self, nombre, direccion, aforo_maximo):
        self._nombre= nombre
        self._direccion= direccion
        self._aforo_maximo= aforo_maximo

    def __str__(self):
        return f"Sede: {self.nombre} | Aforo: {self.aforo_maximo} personas"

    @property
    def nombre(self):
        return self._nombre

    @property
    def aforo_maximo(self):
        return self._aforo_maximo

    @property
    def direccion(self):
        return self._direccion

