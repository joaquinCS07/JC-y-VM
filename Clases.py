class Sede:
    def __init__(self, nombre, direccion, aforo_maximo):
        self.nombre= nombre
        self.direccion= direccion
        self.aforo_maximo= aforo_maximo



class Evento:
    def __init__(self, nombre_evento, fecha, sede):
        self.nombre_evento = nombre_evento
        self.fecha = fecha
        self.sede = sede
        self.entradas_vendidas= []


