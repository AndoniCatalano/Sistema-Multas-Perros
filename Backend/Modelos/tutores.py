from pydantic import BaseModel
from typing import Optional

class Tutor(BaseModel):
    id: int
    nombre: str
    telefono: str
    direccion: str
    dni: str