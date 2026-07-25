from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from typing import Literal

class Multa(BaseModel):
    id: int
    monto: float
    fechahora: Optional[datetime] = None
    perroid: int
    tutorid: int
    descripcion: str
    estado: Literal["P","D"] = "D"