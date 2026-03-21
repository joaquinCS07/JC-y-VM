from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, dni, email, telefono):
        super().__init__(nombre, dni, email)
        self._telefono = telefono
        self._historial_compras = []

    def nueva_compra(self, compra):
        self._historial_compras.append(compra)
        print(f'Compra guardada para: {self._nombre}')

    def mostrar_info(self):
        info_persona = super().mostrar_info()
        return f'{info_persona}, Teléfono: {self._telefono}, Compras: {len(self._historial_compras)}'


    @property
    def telefono(self):
        return self._telefono

@property
def historial_compras(self):
    return self._historial_compras
