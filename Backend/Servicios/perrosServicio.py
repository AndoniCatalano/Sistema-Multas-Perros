import logging
import DTO.perrosDTO as dto
import Repositorios.tutoresRepositorio as repoTutores
import Repositorios.perrosRepositorio as repoPerros
from Modelos.perros import Perro


def buscarPerroId(id:int):
    try:
        perro = repoPerros.buscarPerroId(id)
        if perro is None:
            raise ValueError("Perro no encontrado")

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
            tutor = repoTutores.buscarTutorId(perro.tutorid)
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

def crearPerro(perro: Perro):
    try:
        repoPerros.crearPerro(perro)
        return {"mensaje": "Perro creado exitosamente"}
    except Exception as e:
        logging.error(f"Error al crear perro: {str(e)}")
        raise e

def editarPerro(perro: Perro, id: int):
    try:
        repoPerros.editarPerro(perro, id)
        return {"mensaje": "Perro editado exitosamente"}
    except Exception as e:
        logging.error(f"Error al editar perro {id}: {str(e)}")
        raise e

def eliminarPerro(id: int):
    try:
        repoPerros.eliminarPerro(id)
        return {"mensaje": "Perro eliminado exitosamente"}
    except Exception as e:
        logging.error(f"Error al eliminar perro {id}: {str(e)}")
        raise e