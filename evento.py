class Evento:
    def __init__(self, nombre_evento, fecha, sede):
        self._nombre_evento = nombre_evento
        self._fecha = fecha
        self._sede = sede
        self._entradas_vendidas= []
