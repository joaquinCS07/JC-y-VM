class Persona:

    total_personas = 0

    def __init__(self, nombre, dni, correo):
        self._nombre = nombre
        self._dni = dni
        self._correo = correo
        Persona.total_personas += 1

    def mostrar_info(self):
        return f'Nombre: {self._nombre}, dni: {self._dni}, correo electrónico: {self._correo}'

    @classmethod
    def total_registrados(cls):
        return cls.total_personas

