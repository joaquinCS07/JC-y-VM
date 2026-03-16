from persona import Persona
class Cliente(Persona):
    def __init__(self, nombre, dni, email, telefono):

        super().__init__(nombre, dni, email)
        self._telefono = telefono
        self.historial_compras = []

        def nueva_compra(self, compra):
            self.historial_compras.append(compra)
            print(f'Compra guardada correctamente en el historial del cliente: {self._nombre}')

        def mostrar_info(self):
            info_persona = super().mostrar_info()
            return f'{info_persona}, Teléfono: {self._telefono}, Número de compras realizadas: {len(self._historial_compras)} '
