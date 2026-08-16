from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from typing import Literal

class Multa(BaseModel):

    id:int
    monto:float
    fechahora: Optional[datetime] = None
    estado: Literal["P","D"] = "D"
    descripcion:str
    perroid:int
    tutorid:int

    @classmethod
    def modelo(cls,raw:dict):
        return cls(**raw)

    @classmethod
    def modeloLista(cls,rawLista: list[dict]):
        return [cls(**raw) for raw in rawLista]