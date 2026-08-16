from Modelos.perros import Perro
from Modelos.tutores import Tutor

class perroCompletoDTO:
    def __init__(self, perro:Perro, tutor:Tutor):
        self.raza = perro.raza
        self.genero = perro.genero
        self.nombrePerro = perro.nombrePerro
        self.edad = perro.edad
        self.foto = perro.foto
        self.color = perro.color
        self.nombreTutor = tutor.nombreTutor
        self.direccion = tutor.direccion
        self.telefono = tutor.telefono

class perroListadoDTO:
    def __init__(self, perro:Perro, tutor:Tutor):
        self.id = perro.id
        self.raza = perro.raza
        self.genero = perro.genero
        self.nombrePerro = perro.nombrePerro
        self.edad = perro.edad
        self.foto = perro.foto
        self.color = perro.color
        self.nombreTutor = tutor.nombreTutor

class perroTutorDTO:
    def __init__(self, perro:Perro):
        self.id = perro.id
        self.raza = perro.raza
        self.genero = perro.genero
        self.nombrePerro = perro.nombrePerro
        self.edad = perro.edad
        self.foto = perro.foto
        self.color = perro.color