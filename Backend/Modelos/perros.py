from pydantic import BaseModel

class Perro(BaseModel):
    raza:str
    genero:str
    nombre:str
    edad:int
    foto:str
    tutorid:int
    