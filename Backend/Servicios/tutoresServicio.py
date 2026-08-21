import logging

from DTO.tutorCompletoDTO import tutorCompletoDTO
from DTO.tutorListadoDTO import tutorListadoDTO
import Repositorios.tutoresRepositorio as repo

from Modelos.tutores import Tutor

from sqlalchemy.exc import OperationalError, DatabaseError

def buscarTutorId(id:int):
    try:
        tutor = repo.buscarTutorId(id)
        if tutor is None:
            raise ValueError(f"Tutor no encontrado")
        return tutorCompletoDTO(tutor)

    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")
    
    except Exception as e:
        logging.error(f"Error al obtener tutor: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")

def obtenerTutores(dni: str = None, nombre: str = None, telefono: str = None):
    try:
        tutores = repo.obtenerTutores(dni,nombre,telefono)
        listado = []
        for tutor in tutores:
            listado.append(tutorListadoDTO(tutor))

        return listado

    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except ValueError as ve:
        logging.warning(str(ve))
        raise ve
    
    except Exception as e:
        logging.error(f"Error al obtener tutor: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")
    

def crearTutor(tutor: Tutor):
    try:
        repo.crearTutor(tutor)
        return {"mensaje": "Tutor creado exitosamente"}
    
    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except Exception as e:
        logging.error(f"Error al crear tutor: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")
    
def editarTutor(tutor: Tutor, id: int):
    try:
        repo.editarTutor(tutor, id)
        return {"mensaje": "Tutor editado exitosamente"}
    
    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except Exception as e:
        logging.error(f"Error al editar tutor {id}: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")

def eliminaTutor(id: int):
    try:
        repo.eliminaTutor(id)
        return {"mensaje": "Tutor eliminado exitosamente"}
    
    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")
    
    except Exception as e:
        logging.error(f"Error al eliminar tutor {id}: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")