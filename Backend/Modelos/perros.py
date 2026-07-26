from pydantic import BaseModel

class Perro(BaseModel):
    id:int
    raza:str
    genero:str
    nombre:str
    color:str
    edad:int
    foto:str
    tutorid:int
    