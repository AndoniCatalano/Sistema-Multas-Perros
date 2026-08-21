from Modelos.perros import Perro
from Modelos.tutores import Tutor

class perroTutorDTO:
    def __init__(self, perro:Perro):
        self.id = perro.id
        self.raza = perro.raza
        self.genero = perro.genero
        self.nombrePerro = perro.nombrePerro
        self.edad = perro.edad
        self.foto = perro.foto
        self.color = perro.color