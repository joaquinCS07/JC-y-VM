class Evento:
    def __init__(self, nombre_evento, fecha, sede):
        self._nombre_evento = nombre_evento
        self._fecha = fecha
        self._sede = sede
        self._entradas_vendidas= []

    def calcular_ingresos_totales(self):
        total = 0
        for entrada in self.entradas_vendidas:
            total += entrada.calcular_precio()
        return total


