from entrada import Entrada

class EntradaGeneral(Entrada):
    def __init__(self, id_entrada, precio_base):
        super().__init__(id_entrada, precio_base)
        self._puerta_acceso = "Puerta Principal"

    def calcular_precio(self) -> float:
        return self.precio_base