import Repositorios.tutoresRepositorio as repo
from Modelos.tutores import Tutor

def buscarTutorId(id:int):
    tutor = repo.buscarTutorId(id)
    tutor = dict(tutor)
    tutor.pop("id")
    return tutor

def obtenerTutores(dni: str = None, nombre: str = None, telefono: str = None):
    tutores = repo.obtenerTutores(dni,nombre,telefono)
    listado = []
    for tutor in tutores:
        tutor = dict(tutor)
        listado.append(tutor)
    return listado

def crearTutor(tutor:Tutor):
    repo.crearTutor(tutor)
    return{"mensaje":"tutor creado exitosamente"}
    
def editarTutor(tutor:Tutor, id:int):
    repo.editarTutor(tutor,id)
    return{"mensaje":"tutor editado exitosamente"}

def eliminaTutor(id:int):
    repo.eliminaTutor(id)
    return{"mensaje":"tutor eliminado exitosamente"}
