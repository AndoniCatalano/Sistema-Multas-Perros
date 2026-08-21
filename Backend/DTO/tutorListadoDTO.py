from Modelos.tutores import Tutor

class TutorListado:
    def __init__(self, tutor:Tutor):
        self.id = tutor.id
        self.telefono = tutor.telefono
        self.direccion = tutor.direccion
        self.dni = tutor.dni
        self.nombreTutor = tutor.nombreTutor