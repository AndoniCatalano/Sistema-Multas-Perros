from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from typing import Literal

class MultaBase(BaseModel):
    monto:float
    fechahora: Optional[datetime] = None
    estado: Literal["P","D"] = "D"

    @classmethod
    def modelo(cls,raw:dict):
        return cls(**raw)

    @classmethod
    def modeloLista(cls,rawLista: list[dict]):
        return [cls(**raw) for raw in rawLista]

class MultaListado(MultaBase):
    id:int
    nombreTutor:str

class MultaPerro(MultaBase):
    descripcion:str

class MultaTutor(MultaPerro):
    nombrePerro:str

class MultaCompleta(MultaTutor):
    nombreTutor:str
    direccion:str
    telefono:str

class MultaCrear(MultaBase):
    perroid:int
    tutorid:int
    descripcion:str