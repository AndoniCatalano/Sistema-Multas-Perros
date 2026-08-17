import logging
import DTO.tutoresDTO as dto
import Repositorios.tutoresRepositorio as repo
from Modelos.tutores import Tutor

def buscarTutorId(id:int):
    try:
        tutor = repo.buscarTutorId(id)
        if tutor is None:
            raise ValueError(f"Tutor no encontrado")
        return dto.TutorCompleto(tutor)
    except Exception as e:
        logging.error(f"Error al obtener tutor: {str(e)}")
        raise e

def obtenerTutores(dni: str = None, nombre: str = None, telefono: str = None):
    try:
        tutores = repo.obtenerTutores(dni,nombre,telefono)
        listado = []
        for tutor in tutores:
            listado.append(dto.TutorListado(tutor))

        return listado
    
    except Exception as e:
        logging.error(f"Error al obtener tutor: {str(e)}")
        raise e
    

def crearTutor(tutor: Tutor):
    try:
        repo.crearTutor(tutor)
        return {"mensaje": "Tutor creado exitosamente"}
    except Exception as e:
        logging.error(f"Error al crear tutor: {str(e)}")
        raise e
    
def editarTutor(tutor: Tutor, id: int):
    try:
        repo.editarTutor(tutor, id)
        return {"mensaje": "Tutor editado exitosamente"}
    except Exception as e:
        logging.error(f"Error al editar tutor {id}: {str(e)}")
        raise e

def eliminaTutor(id: int):
    try:
        repo.eliminaTutor(id)
        return {"mensaje": "Tutor eliminado exitosamente"}
    except Exception as e:
        logging.error(f"Error al eliminar tutor {id}: {str(e)}")
        raise e