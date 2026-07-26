from fastapi import APIRouter
import Servicios.multasServicio as servicio
from Modelos.multas import Multa

router = APIRouter()

@router.get("/multas")
def obtenerMultas():
    return servicio.obtenerMultas()

@router.get("/multas/id")
def buscarMultaId(id:int):
    return servicio.buscarMultaId(id)

@router.get("/multas/perroid")
def obtenerMultasPerro(id:int):
    return servicio.obtenerMultasPerro(id)

@router.get("/multas/tutorid")
def obtenerMultasTutor(id:int):
    return servicio.obtenerMultasTutor(id)

@router.post("/multas/crear")
def crearMulta(multa:Multa):
    servicio.crearMulta(multa)

@router.put("/multas/editar")
def editarEstadoMulta(estado:chr, id:int):
    servicio.editarEstadoMulta(estado, id)

@router.delete("/multas/eliminar")
def eliminarMulta(id:int):
    servicio.eliminarMulta(id)
