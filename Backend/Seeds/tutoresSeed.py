# seeders_tutores.py
import logging
import Repositorios.tutoresRepositorio as repoTutores
from Modelos.tutores import Tutor

logging.basicConfig(level=logging.INFO)

def cargar_tutores():
    try:
        tutores = [
            Tutor(nombreTutor="Alberto Gomez", telefono="2234001122", direccion="Colón 1234", dni="24555666"),
            Tutor(nombreTutor="Claudia Martínez", telefono="2235334455", direccion="Mitre 567", dni="27888999"),
            Tutor(nombreTutor="Gastón Ramirez", telefono="2236778899", direccion="Salta 890", dni="31222333"),
            Tutor(nombreTutor="Patricia Sosa", telefono=None, direccion="Libertad 1500", dni="34111222"),
            Tutor(nombreTutor="Marcos Benítez", telefono="2237889900", direccion="Constitución 3200", dni="29444555")
        ]
        
        for tutor in tutores:
            repoTutores.crearTutor(tutor)
            
    except Exception as e:
        logging.error(f"Error al cargar tutores: {str(e)}")
        raise e

if __name__ == "__main__":
    cargar_tutores()