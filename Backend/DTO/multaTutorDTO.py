from Modelos.multas import Multa
from Modelos.perros import Perro

class multaTutorDTO:
    def __init__(self, multa:Multa, perro:Perro):
        self.id = multa.id
        self.monto = multa.monto
        self. fechahora = multa.fechahora
        self.nombrePerro = perro.nombrePerro
        self.descripcion = multa.descripcion
        self.estado = multa.estado