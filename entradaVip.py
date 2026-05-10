from entrada import Entrada
class EntradaVIP(Entrada):
    def __init__(self, id_entrada, precio_base, zona_exclusiva):
        super().__init__(id_entrada, precio_base)
        self.puerta_acceso = "Puerta Prioritaria"
        self.zona_exclusiva = zona_exclusiva

    def calcular_precio(self) -> float:
        return self.precio_base * 1.5