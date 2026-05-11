
# Excepción para los eventos que ya están en la agenda:
class EventoDuplicadoError(Exception):
    pass

class AforoCompletoError(Exception):
    def __init__(self):
        super().__init__("No quedan plazas disponibles para este evento")


class EntradaDuplicadaError(Exception):
    def __init__(self):
        super().__init__("Ya existe una entrada con ese ID")


class PrecioInvalidoError(Exception):
    def __init__(self):
        super().__init__("El precio debe ser mayor que 0")


class EventoInvalidoError(Exception):
    def __init__(self):
        super().__init__("El evento no es válido")

