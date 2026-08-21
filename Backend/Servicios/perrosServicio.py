import logging
from DTO.perroCompletoDTO import perroCompletoDTO
from DTO.perroListadoDTO import perroListadoDTO
from DTO.perroTutorDTO import perroTutorDTO
import Repositorios.tutoresRepositorio as repoTutores
import Repositorios.perrosRepositorio as repoPerros

from Modelos.perros import Perro

from sqlalchemy.exc import OperationalError,DatabaseError

def buscarPerroId(id:int):
    try:
        perro = repoPerros.buscarPerroId(id)
        if perro is None:
            raise ValueError("Perro no encontrado")

        tutor = repoTutores.buscarTutorId(perro.tutorid)
        return perroCompletoDTO(perro,tutor)

    except (OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos al buscar perro: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")
    
    except ValueError as ve:
        logging.warning(str(ve))
        raise ve

    except Exception as e:
        logging.error(f"Error al obtener perro: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")

def ObtenerPerros(color: str = None, genero: str = None, nombre: str = None, raza: str = None):
    try:
        perros = repoPerros.ObtenerPerros(color,genero,nombre,raza)
        listado = []
        for perro in perros:
            try:
                tutor = repoTutores.buscarTutorId(perro.tutorid)
                listado.append(perroListadoDTO(perro,tutor))

            except (OperationalError, DatabaseError) as db_err:
                logging.error(f"Falla en la base de datos al buscar perro: {str(db_err)}")
                continue

        return listado
    
    except (OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos al buscar perro: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")
    
    except Exception as e:
        logging.error(f"Error al obtener perros: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")

def obtenerPerrosTutor(id:int):
    try:
        perros = repoPerros.obtenerPerrosTutor(id)
        listado = []

        for perro in perros:
            listado.append(perroTutorDTO(perro))

        return listado
    
    except (OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos al buscar perro: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")
    
    except Exception as e:
        logging.error(f"Error al obtener perros: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")

def crearPerro(perro: Perro):
    try:
        repoPerros.crearPerro(perro)
        return {"mensaje": "Perro creado exitosamente"}

    except (OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos al buscar perro: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")
    
    except Exception as e:
        logging.error(f"Error al crear perro: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")

def editarPerro(perro: Perro, id: int):
    try:
        repoPerros.editarPerro(perro, id)
        return {"mensaje": "Perro editado exitosamente"}
    
    except (OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos al buscar perro: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except Exception as e:
        logging.error(f"Error al editar perro {id}: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")

def eliminarPerro(id: int):
    try:
        repoPerros.eliminarPerro(id)
        return {"mensaje": "Perro eliminado exitosamente"}
    
    except (OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos al buscar perro: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except Exception as e:
        logging.error(f"Error al eliminar perro {id}: {str(e)}")
        raise RuntimeError("Ocurrió un error interno al procesar la solicitud")