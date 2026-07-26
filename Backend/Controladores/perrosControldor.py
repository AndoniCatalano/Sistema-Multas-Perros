from fastapi import APIRouter
import Servicios.perrosServicio as servicio
from Modelos.perros import Perro

router = APIRouter()

@router.get("/perros")
def obtenerPerros():
    return servicio.obtenerPerros()

@router.get("/perros/id")
def buscarPerroId(id:int):
    return servicio.buscarPerroId(id)

@router.get("/perros/color")
def buscarPerroColor(color: str):
    return servicio.buscarPerroColor(color)

@router.get("/perros/genero")
def buscarPerroGenero(genero: str):
    return servicio.buscarPerroGenero(genero)

@router.get("/perros/nombre")
def buscarPerroNombre(nombre: str):
    return servicio.buscarPerroNombre(nombre)

@router.get("/perros/raza")
def buscarPerroRaza(raza: str):
    return servicio.buscarPerroRaza(raza)

@router.get("/perros/tutorid")
def obtenerPerrosTutor(id:int):
    return servicio.obtenerPerrosTutor(id)

@router.post("/perros/crear")
def crearPerro(perro:Perro):
    servicio.crearPerro(perro)

@router.put("/perros/editar")
def editarPerro(perro:Perro, id:int):
    servicio.editarPerro(perro,id)

@router.delete("/perros/eliminar")
def eliminarPerro(id:int):
    servicio.eliminarPerro(id)
