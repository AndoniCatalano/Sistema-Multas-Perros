# seeders_multas.py
import logging
from datetime import datetime
import Repositorios.multasRepositorio as repoMultas
from Modelos.multas import Multa

logging.basicConfig(level=logging.INFO)

def cargar_multas():
    try:
        multas = [
            Multa(
                monto=35000.00,
                fechahora=datetime(2026, 3, 10, 15, 30),
                descripcion="El can atacó y mordió a un transeúnte en la vía pública provocando lesiones en una pierna",
                estado="Pendiente",
                perroid=1,
                tutorid=1
            ),
            Multa(
                monto=50000.50,
                fechahora=datetime(2026, 4, 12, 18, 00),
                descripcion="Agresión física a un peatón al escaparse del domicilio sin bozal ni correa",
                estado="Pendiente",
                perroid=2,
                tutorid=2
            ),
            Multa(
                monto=42000.00,
                fechahora=datetime(2026, 5, 20, 11, 15),
                descripcion="Mordedura a vecino que intentaba ingresar a la propiedad, el animal se encontraba suelto en la entrada",
                estado="Pagada",
                perroid=3,
                tutorid=3
            ),
            Multa(
                monto=28000.00,
                fechahora=datetime(2026, 6, 2, 9, 45),
                descripcion="Intento de ataque a un menor en la plaza del barrio, sin lesiones graves pero con riesgo evidente",
                estado="Pendiente",
                perroid=4,
                tutorid=4
            ),
            Multa(
                monto=60000.00,
                fechahora=datetime(2026, 6, 18, 20, 10),
                descripcion="Ataque feroz a un repartidor en bicicleta en la puerta del domicilio",
                estado="Pagada",
                perroid=5,
                tutorid=5
            )
        ]

        for multa in multas:
            repoMultas.crearMulta(multa)

    except Exception as e:
        logging.error(f"Error al cargar multas: {str(e)}")
        raise e

if __name__ == "__main__":
    cargar_multas()