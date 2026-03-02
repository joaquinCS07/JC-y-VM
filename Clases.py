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
        return f"Evento: {self.nombre} | Fecha: {self.fecha} | Lugar: {self.sede.nombre}"


