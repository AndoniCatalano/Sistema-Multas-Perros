from fastapi import APIRouter
import Servicios.tutoresServicio as servicio
from Modelos.tutores import Tutor

router = APIRouter()


@router.get("/tutores/buscar")
def buscarTutorId(id: int):
    return servicio.buscarTutorId(id)


@router.get("/tutores")
def obtenerTutores(dni: str = None, nombre: str = None, telefono: str = None):
    return servicio.obtenerTutores(dni, nombre, telefono)


@router.post("/tutores")
def crearTutor(tutor: Tutor):
    return servicio.crearTutor(tutor)


@router.put("/tutores")
def editarTutor(tutor: Tutor, id: int):
    return servicio.editarTutor(tutor, id)


@router.delete("/tutores")
def eliminaTutor(id: int):
    return servicio.eliminaTutor(id)