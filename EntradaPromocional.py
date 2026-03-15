from EntradaGeneral import EntradaGeneral
from Promocion import Promocion

class EntradaPromocional(EntradaGeneral, Promocion):
    def __init__(self, id_entrada, precio_base, nombre_promo, descuento):
        EntradaGeneral.__init__(self, id_entrada, precio_base)
        Promocion.__init__(self, nombre_promo, descuento)

    def calcular_precio_final(self):
        precio_final = self.aplicar_descuento(self.precio_base)
        return precio_final

    def __str__(self):
        estado = "Vendida" if self.vendida else "Disponible"
        return f"Entrada Promocional #{self.id_entrada} | Promo: {self.nombre_promo} | Precio Final: {self.calcular_precio_final()}€ | {estado}"

    def __repr__(self):
        return f"EntradaPromocional({self.id_entrada}, {self.precio_base}, '{self.nombre_promo}', {self.descuento})"