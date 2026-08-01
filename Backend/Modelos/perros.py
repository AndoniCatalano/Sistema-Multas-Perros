from pydantic import BaseModel

class Perro(BaseModel):
    id:int
    raza:str
    genero:str
    nombrePerro:str
    color:str
    edad:str
    foto:str
    tutorid:int
    