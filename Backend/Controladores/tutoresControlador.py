from fastapi import APIRouter
import Servicios.tutoresServicio as servicio
from Modelos.tutores import Tutor

router = APIRouter()

@router.get("/tutores")
def obtenerTutores():
    return servicio.obtenerTutores()

@router.get("/tutores/id")
def buscarTutorId(id: int):
    return servicio.buscarTutorId(id)

@router.get("/tutores/dni")
def buscarTutorDni(dni: str):
    return servicio.buscarTutorDni(dni)

@router.get("/tutores/nombre")
def buscarTutorNombre(nombre: str):
    return servicio.buscarTutorNombre(nombre)

@router.get("/tutores/telefono")
def buscarTutorTelefono(telefono: str):
    return servicio.buscarTutorTelefono(telefono)

@router.post("/tutores/crear")
def crearTutor(tutor: Tutor):
    servicio.crearTutor(tutor)

@router.put("/tutores/editar")
def editarTutor(tutor: Tutor, id: int):
    servicio.editarTutor(tutor, id)

@router.delete("/tutores/eliminar")
def eliminaTutor(id: int):
    servicio.eliminaTutor(id)