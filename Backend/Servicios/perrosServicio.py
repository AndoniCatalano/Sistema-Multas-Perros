import Repositorios.perrosRepositorio as repo

def listarPerros():
    perros = repo.obtenerPerros()
    if len(perros) == 0:
        return {"mensaje":"no hay perros registrados"}
    else:
        return perros

    
def buscarPerro(id:int):
    perro = repo.buscarId(id)