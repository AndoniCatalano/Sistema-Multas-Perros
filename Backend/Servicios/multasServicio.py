##TRY CATCH/THROW manejo de errores###
import logging
import Repositorios.multasRepositorio as repoMultas
import Repositorios.perrosRepositorio as repoPerros
import Repositorios.tutoresRepositorio as repoTutores
from DTO.multaCompletaDTO import multaCompletaDTO
from DTO.multaListaDTO import multaListaDTO
from DTO.multaPerroDTO import multaPerroDTO
from DTO.multaTutorDTO import multaTutorDTO

from Modelos.multas import Multa 

from sqlalchemy.exc import OperationalError, DatabaseError


#ademas debe traer nombre del perro y tutor
#direccion y telefono
def buscarMultaId(id:int):

    try:
        multa = repoMultas.buscarMultaId(id)
        if multa is None:
            raise ValueError(f"Multa no encontrada")

        perro = repoPerros.buscarPerroId(multa.perroid)
        tutor = repoTutores.buscarTutorId(multa.tutorid)

        if perro is None or tutor is None:
            raise ValueError(f"La multa existe pero no existe el perro y/o tutor")

        return multaCompletaDTO(multa,perro,tutor)

    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except ValueError as ve:
        logging.warning(str(ve))
        raise ve

    except Exception as e:
        logging.error(f"Error inesperado al buscar la multa: {str(e)}")
        raise RuntimeError("Ocurrio un error interno al procesar la solicitud")

#ademas debe traer el nombre del tutor
def obtenerMultas(anio: int = None, mes: int = None, dia: int = None, hora: int = None, estado: str = None):
    try:
        multas = repoMultas.obtenerMultas(anio,mes,dia,hora,estado)
        listado = []

        for multa in multas:
            try:
                tutor = repoTutores.buscarTutorId(multa.tutorid)
                listado.append(multaListaDTO(multa,tutor))
            except (OperationalError, DatabaseError) as db_err:
                raise logging.error(f"Falla en la base de datos: {str(db_err)}")
        return listado

    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except Exception as e:
        logging.error(f"Error inesperado al buscar la/s multa/s: {str(e)}")
        raise RuntimeError("Ocurrio un error interno al procesar la solicitud")


def obtenerMultasPerro(id:int):
    try:
        multas = repoMultas.obtenerMultasPerro(id)
        listado = []

        for multa in multas:
            listado.append(multaPerroDTO(multa))

        return listado

    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except Exception as e:
        logging.error(f"Error inesperado al buscar la/s multa/s: {str(e)}")
        raise RuntimeError("Ocurrio un error interno al procesar la solicitud")

def obtenerMultasTutor(id:int):
    try:
        listado = []
        multas = repoMultas.obtenerMultasTutor(id)

        for multa in multas:
            listado.append(multaTutorDTO(multa))

        return listado

    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except Exception as e:
        logging.error(f"Error al obtener multas: {str(e)}")
        raise RuntimeError("Ocurrio un error interno al procesar la solicitud")

def crearMulta(multa:Multa):
    try:
        repoMultas.crearMulta(multa)
        return {"mensaje":"multa creada exitosamente"}

    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except Exception as e:
        logging.error(f"Error al crear multa: {str(e)}")
        raise RuntimeError("Ocurrio un error interno al procesar la solicitud")

def editarEstadoMulta(estado: chr, id: int):
    try:
        repoMultas.editarEstadoMulta(estado,id)
        return {"mensaje":"multa editada exitosamente"}
    
    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except Exception as e:
        logging.error(f"Error al eliminar multa: {str(e)}")
        raise RuntimeError("Ocurrio un error interno al procesar la solicitud")

def eliminarMulta(id):
    try:
        repoMultas.eliminarMulta(id)
        return {"mensaje":"multa eliminada exitosamente"}

    except(OperationalError, DatabaseError) as db_err:
        logging.critical(f"Falla en la base de datos: {str(db_err)}")
        raise RuntimeError("Servicio de base de datos no disponible temporalmente")

    except Exception as e:
        logging.error(f"Error al editar multa: {str(e)}")
        raise RuntimeError("Ocurrio un error interno al procesar la solicitud")
