from excepciones import AforoCompletoError, EntradaDuplicadaError

class Evento:
    def __init__(self, nombre_evento, fecha, sede):
        self._nombre_evento = nombre_evento
        self._fecha = fecha
        self._sede = sede
        self._entradas_vendidas= []

    def calcular_ingresos_totales(self):
        total = 0
        for entrada in self._entradas_vendidas:
            total += entrada.calcular_precio()
        return total

    def agregar_venta(self, entrada): 
        
        self._entradas_vendidas.append(entrada)
        entrada.marcar_como_vendida()

# -- Manejo de Errores: -- 
# Control de aforo: 
        if len(self._entradas_vendidas) >= self._sede.aforo_maximo:
            raise AforoCompletoError()
# Control Ids duplicados: 
        for e in self._entradas_vendidas:
            if e.id_entrada == entrada.id_entrada:
                raise EntradaDuplicadaError()
        
    def __str__(self):
        return f"{self._nombre_evento} - {self._fecha} - {self._sede.nombre}"
     
    def __add__(self, otro_evento):
        return self.calcular_ingresos_totales() + otro_evento.calcular_ingresos_totales()


