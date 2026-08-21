from Modelos.multas import Multa
from Modelos.perros import Perro
from Modelos.tutores import Tutor 

class multaCompletaDTO:
    def __init__(self, multa:Multa, perro:Perro, tutor:Tutor):
        self.estado = multa.estado
        self.monto = multa.monto
        self.descripcion = multa.descripcion
        self.fechahora = multa.fechahora
        self.direccion = tutor.direccion
        self.telefono = tutor.telefono
        self.nombreTutor = tutor.nombreTutor
        self.nombrePerro = perro.nombrePerro
