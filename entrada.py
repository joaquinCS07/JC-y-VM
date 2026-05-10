from abc import ABC, abstractmethod

class Entrada(ABC):
    def __init__(self, id_entrada: int, precio_base: float):
        self._id_entrada = id_entrada
        self.precio_base = precio_base
        self._vendida = False

    @abstractmethod
    def calcular_precio(self) -> float:
        pass

    def marcar_como_vendida(self):
        self._vendida = True

    def __str__(self):
        estado = 'Vendida' if self._vendida else 'Disponible'
        return f"Entrada #{self.id_entrada} | Precio: {self.precio_base}€ | {estado}"



