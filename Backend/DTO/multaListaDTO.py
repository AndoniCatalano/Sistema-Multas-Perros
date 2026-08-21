from Modelos.multas import Multa
from Modelos.tutores import Tutor 

class multaListaDTO:
    def __init__(self, multa:Multa, tutor:Tutor):
        self.id = multa.id
        self.monto = multa.monto
        self.fechahora = multa.fechahora
        self.estado = multa.estado
        self.nombreTutor = tutor.nombreTutor