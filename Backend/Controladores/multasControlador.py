from fastapi import APIRouter
import Servicios.multasServicio as servicio
from Modelos.multas import Multa

router = APIRouter()

@router.get("/multas/buscar")
def buscarMultaId(id: int):
    return servicio.buscarMultaId(id)

@router.get("/multas")
def obtenerMultas(anio: int = None, mes: int = None, dia: int = None, hora: int = None, estado: str = None):
    return servicio.obtenerMultas(anio, mes, dia, hora, estado)


@router.get("/multas/perro")
def obtenerMultasPerro(id: int):
    return servicio.obtenerMultasPerro(id)


@router.get("/multas/tutor")
def obtenerMultasTutor(id: int):
    return servicio.obtenerMultasTutor(id)


@router.post("/multas")
def crearMulta(multa: Multa):
    return servicio.crearMulta(multa)


@router.patch("/multas")
def editarEstadoMulta(id: int, estado: str):
    return servicio.editarEstadoMulta(id, estado)


@router.delete("/multas")
def eliminarMulta(id: int):
    return servicio.eliminarMulta(id)