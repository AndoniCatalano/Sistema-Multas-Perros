from pydantic import BaseModel
from typing import Optional

class Tutor(BaseModel):
    id:int
    nombreTutor: str
    telefono: str
    direccion: str
    dni: str

    @classmethod
    def modelo(cls,raw:dict):
        return cls(**raw)

    @classmethod
    def modeloLista(cls,rawLista:list[dict]):
        return[cls(**raw) for raw in rawLista]