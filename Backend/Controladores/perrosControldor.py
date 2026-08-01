from fastapi import APIRouter
import Servicios.perrosServicio as servicio
from Modelos.perros import Perro

router = APIRouter()


@router.get("/perros/buscar")
def buscarPerroId(id: int):
    return servicio.buscarPerroId(id)


@router.get("/perros")
def obtenerPerros(color: str = None, genero: str = None, nombre: str = None, raza: str = None):
    return servicio.obtenerPerros(color, genero, nombre, raza)


@router.get("/perros/tutor")
def obtenerPerrosTutor(id: int):
    return servicio.obtenerPerrosTutor(id)


@router.post("/perros")
def crearPerro(perro: Perro):
    return servicio.crearPerro(perro)


@router.put("/perros")
def editarPerro(perro: Perro, id: int):
    return servicio.editarPerro(perro, id)


@router.delete("/perros")
def eliminarPerro(id: int):
    return servicio.eliminarPerro(id)