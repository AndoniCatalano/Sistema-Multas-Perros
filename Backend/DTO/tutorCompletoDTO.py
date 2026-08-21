from Modelos.tutores import Tutor

class TutorCompleto:
    def __init__(self, tutor:Tutor):
        self.telefono = tutor.telefono
        self.direccion = tutor.direccion
        self.dni = tutor.dni
        self.nombreTutor = tutor.nombreTutor
