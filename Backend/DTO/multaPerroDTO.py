from Modelos.multas import Multa

class multaPerroDTO:
    def __init__(self, multa:Multa):
        self.id = multa.id
        self.fechahora = multa.fechahora
        self.monto = multa.monto
        self.descripcion = multa.descripcion
        self.estado = multa.estado