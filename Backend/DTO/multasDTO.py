###MODELO SOLO CON ATRIBUTOS DE LECTURA NO EDITABLE
from Modelos.multas import Multa
from Modelos.perros import Perro
from Modelos.tutores import Tutor 

class multaCompletaDTO:
    def __init__(self, multa:Multa, perro:Perro, tutor:Tutor):
        self.id = multa.id
        self.estado = multa.estado
        self.monto = multa.monto
        self.descripcion = multa.descripcion
        self.fechahora = multa.fechahora
        self.direccion = tutor.direccion
        self.telefono = tutor.telefono
        self.nombreTutor = tutor.nombreTutor
        self.nombrePerro = perro.nombrePerro

class multaListaDTO:
    def __init__(self, multa:Multa, tutor:Tutor):
        self.id = multa.id
        self.monto = multa.monto
        self.fechahora = multa.fechahora
        self.estado = multa.estado
        self.nombreTutor = tutor.nombreTutor

class multaPerroDTO:
    def __init__(self, multa:Multa):
        self.id = multa.id
        self.fechahora = multa.fechahora
        self.monto = multa.monto
        self.descripcion = multa.descripcion
        self.estado = multa.estado

class multaTutorDTO:
    def __init__(self, multa:Multa, perro:Perro):
        self.id = multa.id
        self.monto = multa.monto
        self. fechahora = multa.fechahora
        self.nombrePerro = perro.nombrePerro
        self.descripcion = multa.descripcion
        self.estado = multa.estado