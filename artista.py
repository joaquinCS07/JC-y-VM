from persona import Persona
from agenda import Agenda

class Artista(Persona):
    def __init__(self, nombre, dni, correo, genero):
        super().__init__(nombre, dni)
        self.genero= genero
        self._correo = correo
        self.agenda= Agenda()

    def agregar_a_agenda(self, evento):  #Añade un evento al objeto agenda
        self._agenda.agregar_evento(evento)

    def cancelar_de_agenda(self, evento):  #Sirve para eliminarun evento del objeto agenda
        self._agenda.cancelar_evento(evento)

    def ver_agenda(self): #Devuelve los eventos programados del artista
        return self._agenda.mostrar_eventos()

    def __str__(self):
        return f'Arista: {self.nombre}, Dni: {self.dni}, Genero: {self.genero}'