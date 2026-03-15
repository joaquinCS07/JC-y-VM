class Promocion:
    def __init__(self, nombre_promo, descuento):
        self.nombre_promo = nombre_promo
        self.descuento = descuento  # Cantidad fija a restar (ej: 10€)

    def aplicar_descuento(self, precio):
        return precio - self.descuento