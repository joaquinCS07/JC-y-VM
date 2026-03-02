class Sede:
    def __init__(self, nombre, direccion, aforo_maximo):
        self.nombre= nombre
        self.direccion= direccion
        self.aforo_maximo= aforo_maximo

    def __str__(self):
        return f"Sede: {self.nombre} | Aforo: {self.aforo_maximo} personas"

class Evento:
    def __init__(self, nombre_evento, fecha, sede):
        self.nombre_evento = nombre_evento
        self.fecha = fecha
        self.sede = sede
        self.entradas_vendidas= []

    def __str__(self):
        return f"Evento: {self.nombre_evento} | Fecha: {self.fecha} | Lugar: {self.sede.nombre}"

class Entrada:
    def __init__(self, id_entrada, precio_base):
        self.id_entrada = id_entrada
        self.precio_base = precio_base

    def __str__(self):
        return f"Entrada #{self.id_entrada} | Precio: {self.precio_base}€"

class EntradaGeneral(Entrada):
    def __init__(self, id_entrada, precio_base):
        # super().__init__ llama al constructor de la clase padre (Entrada)
        super().__init__(id_entrada, precio_base)
        self.puerta_acceso = "Puerta Principal"

class EntradaVIP(Entrada):
    def __init__(self, id_entrada, precio_base, zona_exclusiva):
        super().__init__(id_entrada, precio_base)
        self.puerta_acceso = "Puerta Prioritaria"
        self.zona_exclusiva = zona_exclusiva


