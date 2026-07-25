from fastapi import APIRouter
import Servicios.perrosServicio as servicio

router = APIRouter()

@router.get("/perros")
def mostrarPerros():
    return servicio.listarPerros()