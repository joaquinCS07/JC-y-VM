from Persona import Persona

class Artista(Persona):
    def __init__(self, nombre, dni, genero):
        super().__init__(nombre, dni)
        self.genero= genero
        self.agenda=[]

    def agregar_evento(self, evento):
        if evento not in self.agenda:
            self.agenda.append(evento)
        else:
            print("Error: El evento ya está en la agenda.")

    def __str__(self):
        return f'Arista: {self.nombre}, Dni: {self.dni}, Genero: {self.genero}'