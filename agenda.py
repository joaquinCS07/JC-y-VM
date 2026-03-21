
class Agenda:

    def __init__(self):
        self._eventos = []

    def agregar_evento(self, evento):
        if evento not in self._eventos:
            self._eventos.append(evento)
            print("Evento añadido a la agenda con éxito.")
        else:
            print("Error: El evento ya está en la agenda.")

    def cancelar_evento(self, evento):
        if evento in self._eventos:
            self._eventos.remove(evento)
            print("Evento cancelado y eliminado de la agenda.")
        else:
            print("Error: El evento no existe en esta agenda.")

    def mostrar_eventos(self):
        if not self._eventos:
            return "La agenda está vacía."

        return "\n".join([str(evento) for evento in self._eventos])