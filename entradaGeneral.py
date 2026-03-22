    from entrada import Entrada

class EntradaGeneral(Entrada):
    def __init__(self, id_entrada, precio_base):
        super().__init__(id_entrada, precio_base)
        self._puerta_acceso = "Puerta Principal"

    def calcular_precio_final(self):
        return self._precio_base