# seeders_perros.py
import logging
import Repositorios.perrosRepositorio as repoPerros
from Modelos.perros import Perro

logging.basicConfig(level=logging.INFO)

def cargar_perros():
    try:
        perros = [
            Perro(nombrePerro="Zeus", raza="Pitbull", genero="Macho", edad=4, foto="zeus.jpg", tutorid=1),
            Perro(nombrePerro="Kira", raza="Rottweiler", genero="Hembra", edad=3, foto="kira.jpg", tutorid=2),
            Perro(nombrePerro="Tyson", raza="Dogo Argentino", genero="Macho", edad=5, foto="tyson.jpg", tutorid=3),
            Perro(nombrePerro="Simba", raza="Ovejero Alemán", genero="Macho", edad=2, foto="simba.jpg", tutorid=4),
            Perro(nombrePerro="Negra", raza="Mestizo", genero="Hembra", edad=6, foto="negra.jpg", tutorid=5)
        ]

        for perro in perros:
            repoPerros.crearPerro(perro)

    except Exception as e:
        logging.error(f"Error al cargar perros: {str(e)}")
        raise e

if __name__ == "__main__":
    cargar_perros()