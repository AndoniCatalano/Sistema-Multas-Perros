import Repositorios.perrosRepositorio as repo
from Modelos.perros import Perro


def buscarPerroId(id:int):
    perro = repo.buscarPerroId(id)
    perro = dict(perro)
    perro.pop("id")
    perro.pop("tutorid")
    return perro

def ObtenerPerros(color: str = None, genero: str = None, nombre: str = None, raza: str = None):
    perros = repo.ObtenerPerros(color,genero,nombre,raza)
    listado = []
    for perro in perros:
        perro = dict(perro)
        listado.append(perro)
    return listado

def obtenerPerrosTutor(id:int):
    perros = repo.obtenerPerrosTutor(id)
    listado = []
    for perro in perros:
        perro = dict(perro)
        perro.pop("id")
        perro.pop("tutorid")
        listado.append("tutorid")

def crearPerro(perro:Perro):
    repo.crearPerro(perro)
    return{"mensaje":"perro creado exitosamente"}

def editarPerro(perro:Perro, id:int):
    repo.editarPerro(perro, id)
    return{"mensaje":"perro editado exitosamente"}

def eliminarPerro(id:int):
    repo.eliminarPerro(id)
    return{"mensaje":"perro eliminado exitosamente"}

