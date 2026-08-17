##TRY CATCH/THROW manejo de errores###
import logging
import Repositorios.multasRepositorio as repoMultas
import Repositorios.perrosRepositorio as repoPerros
import Repositorios.tutoresRepositorio as repoTutores
import DTO.multasDTO as dto

from Modelos.multas import Multa 



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

        return dto.multaCompletaDTO(multa,perro,tutor)

    except Exception as e:
        logging.error(f"Error al buscar la multa: {str(e)}")
        raise e 

#ademas debe traer el nombre del tutor
def obtenerMultas(anio: int = None, mes: int = None, dia: int = None, hora: int = None, estado: str = None):
    try:
        multas = repoMultas.obtenerMultas(anio,mes,dia,hora,estado)
        listado = []

        for multa in multas:
            tutor = repoTutores.buscarTutorId(multa.tutorid)
            listado.append(dto.multaListaDTO(multa,tutor))

        return listado

    except Exception as e:
        logging.error(f"Error al obtener multas: {str(e)}")
        raise e


def obtenerMultasPerro(id:int):
    try:
        multas = repoMultas.obtenerMultasPerro(id)
        listado = []

        for multa in multas:
            listado.append(dto.multaPerroDTO(multa))

        return listado

    except Exception as e:
        logging.error(f"error al obtener multas:{str(e)}")
        raise e

def obtenerMultasTutor(id:int):
    try:
        listado = []
        multas = repoMultas.obtenerMultasTutor(id)

        for multa in multas:
            listado.append(dto.multaTutorDTO(multa))

        return listado

    except Exception as e:
        logging.error(f"Error al obtener multas: {str(e)}")
        raise e

def crearMulta(multa:Multa):
    repoMultas.crearMulta(multa)
    return {"mensaje":"multa creada exitosamente"}

def editarEstadoMulta(estado: chr, id: int):
    repoMultas.editarEstadoMulta(estado,id)
    return {"mensaje":"multa editada exitosamente"}

def eliminarMulta(id):
    repoMultas.eliminarMulta(id)
    return {"mensaje":"multa eliminada exitosamente"}
