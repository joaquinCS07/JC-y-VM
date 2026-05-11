from abc import ABC, abstractmethod

from excepciones import PrecioInvalidoError

class Entrada(ABC):

    def __init__(self, id_entrada: int, precio_base: float):
        self._id_entrada = id_entrada
        self._vendida = False
        if precio_base <= 0:
            raise PrecioInvalidoError()

        self._precio_base = precio_base

    @property
    def id_entrada(self):
        return self._id_entrada

    @property
    def precio_base(self):
        return self._precio_base

    @abstractmethod
    def calcular_precio(self) -> float:
        pass

    def marcar_como_vendida(self):
        self._vendida = True

    def __str__(self):
        estado = "Vendida" if self._vendida else "Disponible"

        return f"Entrada #{self._id_entrada} | Precio: {self._precio_base}€ | {estado}"

    def __eq__(self, other):
        return self._id_entrada == other._id_entrada



