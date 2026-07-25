from database import cursor, conexion
from Modelos.perros import Perro


def obtenerPerros():
    cursor.execute("SELECT * FROM perros")
    return cursor.fetchall()

def buscarId(id:int):
    sql = """
    SELECT * FROM perros
    WHERE id = %s
    """
    cursor.execute(sql,(id,))
    return cursor.fetchone()

def crearPerro(perro:Perro):
    sql = """
     INSERT INTO perros (raza, genero, nombre, edad, foto, tutorid)
     VALUES (%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(sql,(perro.raza, perro.genero, perro.nombre, perro.edad, perro.foto, perro.tutorid))
    conexion.commit()

def editarPerro(perro:Perro, id:int):
    sql = """
    UPDATE perros 
    SET raza = %s, 
        genero = %s,
        nombre = %s,
        edad = %s, 
        foto = %s, 
        tutorid = %s
    WHERE id = %s
    """
    cursor.execute(sql,(perro.raza, perro.genero, perro.nombre, perro.edad, perro.foto, perro.tutorid,id))
    conexion.commit()

def eliminarPerro(id:int):
    sql = """
    DELETE FROM perros
    WHERE id = %s
    """
    cursor.execute(sql,(id,))
    conexion.commit()
