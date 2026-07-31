import Repositorios.multasRepositorio as repo

def buscarMultaId(id:int):
    multa = repo.buscarMultaId(id)

    if multa is None:
        return None
    else:
        dict(multa)
        multa.pop("id")
        return multa
    
def obtenerMultas(anio: int = None, mes: int = None, dia: int = None, hora: int = None, estado: str = None):
    multas = repo.obtenerMultas(anio,mes,dia,hora,estado)

    listado = []
    for multa in multas:
        multa = dict(multa)
        multa.pop("descripcion",None)
        multa.pop("perroid")
        multa.pop("tutorid")
        listado.append(multa)
    return listado

def obtenerMultasPerro(id:int):
    multas = repo.obtenerMultasPerro(id)

    listado = []
    for multa in multas:
        multa = dict(multa)
        multa.pop("id")
        multa.pop("perroid")
        multa.pop("tutorid")
        listado.append(multa)
    return listado

def obtenerMultasTutor(id:int):
    multas = repo.obtenerMultasTutor(id)

    listado = []
    for multa in multas:
        multa = dict(multa)
        multa.pop("id")
        multa.pop("perroid")
        multa.pop("tutorid")
        listado.append(multa)
    return listado