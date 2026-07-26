from database import cursor, conexion
from Modelos.perros import Perro


def obtenerPerros():
    cursor.execute("SELECT * FROM perros")
    return cursor.fetchall()

def buscarPerroId(id:int):
    sql = """
    SELECT * FROM perros
    WHERE id = %s
    """
    cursor.execute(sql,(id,))
    return cursor.fetchone()

def buscarPerroColor(color: str):
    sql = """
    SELECT * FROM perros
    WHERE color ILIKE %s
    """
    cursor.execute(sql, (f"%{color}%",))
    return cursor.fetchall()


def buscarPerroGenero(genero: str):
    sql = """
    SELECT * FROM perros
    WHERE genero = %s
    """
    cursor.execute(sql, (genero,))
    return cursor.fetchall()


def buscarPerroNombre(nombre: str):
    sql = """
    SELECT * FROM perros
    WHERE nombre ILIKE %s
    """
    cursor.execute(sql, (f"%{nombre}%",))
    return cursor.fetchall()


def buscarPerroRaza(raza: str):
    sql = """
    SELECT * FROM perros
    WHERE raza ILIKE %s
    """
    cursor.execute(sql, (f"%{raza}%",))
    return cursor.fetchall()

def obtenerPerrosTutor(id:int):
    sql = """
    SELECT * FROM perros
    WHERE tutorid = %s
    """
    cursor.execute(sql,(id,))
    return cursor.fetchall()

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
    cursor.execute(sql,(perro.raza, perro.genero, perro.nombre, perro.edad, perro.foto,id))
    conexion.commit()

def eliminarPerro(id:int):
    sql = """
    DELETE FROM perros
    WHERE id = %s
    """
    cursor.execute(sql,(id,))
    conexion.commit()