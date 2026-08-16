import logging
import DTO.perrosDTO as dto
import Repositorios.tutoresRepositorio as repoTutores
import Repositorios.perrosRepositorio as repoPerros
from Modelos.perros import Perro


def buscarPerroId(id:int):
    try:
        perro = repoPerros.buscarPerroId(id)
        if perro is None:
            return ValueError("Perro no encontrado")

        tutor = repoTutores.buscarTutorId(perro.tutorid)
        return dto.perroCompletoDTO(perro,tutor)
 
    except Exception as e:
        logging.error(f"Error al obtener perro: {str(e)}")
        raise e

def ObtenerPerros(color: str = None, genero: str = None, nombre: str = None, raza: str = None):
    try:
        perros = repoPerros.ObtenerPerros(color,genero,nombre,raza)
        listado = []
        for perro in perros:
            tutor = repoTutores.obtenerTutores(perro.tutorid)
            listado.append(dto.perroListadoDTO(perro,tutor))

        return listado

    except Exception as e:
        logging.error(f"Error al obtener perros: {str(e)}")
        raise e

def obtenerPerrosTutor(id:int):
    try:
        perros = repoPerros.obtenerPerrosTutor(id)
        listado = []

        for perro in perros:
            listado.append(dto.perroTutorDTO(perro))

        return listado

    except Exception as e:
        logging.error(f"Error al obtener perros: {str(e)}")
        raise e

def crearPerro(perro:Perro):
    repoPerros.crearPerro(perro)
    return{"mensaje":"perro creado exitosamente"}

def editarPerro(perro:Perro, id:int):
    repoPerros.editarPerro(perro, id)
    return{"mensaje":"perro editado exitosamente"}

def eliminarPerro(id:int):
    repoPerros.eliminarPerro(id)
    return{"mensaje":"perro eliminado exitosamente"}

