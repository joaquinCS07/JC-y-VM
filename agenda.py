from excepciones import EventoDuplicadoError

class Agenda:

    def __init__(self):
        self._eventos = []

    def agregar_evento(self, evento):
        if evento in self._eventos:
            raise EventoDuplicadoError("El evento ya está en la agenda")
        self._eventos.append(evento)


    def cancelar_evento(self, evento):
        if evento not in self._eventos:
            raise ValueError("El evento no existe en la agenda")
        self._eventos.remove(evento)

    def mostrar_eventos(self):
        if not self._eventos:
            return "La agenda está vacía."

        return "\n".join([str(evento) for evento in self._eventos])