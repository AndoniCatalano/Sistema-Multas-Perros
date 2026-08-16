from pydantic import BaseModel

class Perro(BaseModel):

    id:int
    tutorid:int
    raza:str
    genero:str
    nombrePerro:str
    color:str
    edad:str
    foto:str
    
    @classmethod
    def modelo(cls,raw:dict):
        return cls(**raw)

    @classmethod
    def modeloLista(cls,rawLista: list[dict]):
        return[cls(**raw) for raw in rawLista]