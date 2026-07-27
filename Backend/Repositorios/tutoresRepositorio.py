from Modelos.tutores import Tutor
from database import cursor, conexion


def obtenerTutores():
    cursor.execute("SELECT * FROM tutores")
    return cursor.fetchall() 

def buscarTutorId(id:int):
    sql = """
    SELECT * FROM tutores
    WHERE id = %s
    """
    cursor.execute (sql,(id,))
    return cursor.fetchone()

def buscarTutores(dni: str = None, nombre: str = None, telefono: str = None):
    sql = "SELECT * FROM tutores"

    if dni is not None:
        sql += " WHERE dni = %s"
        cursor.execute(sql, (dni,))
        return cursor.fetchone()
    elif telefono is not None:
        sql += " WHERE telefono = %s"
        cursor.execute(sql, (telefono,))
        return cursor.fetchone()
    elif nombre is not None:
        sql += " WHERE nombre LIKE %s"
        cursor.execute(sql, (f"%{nombre}%",))
        return cursor.fetchall()
    else:
        cursor.execute(sql)
        return cursor.fetchall()


def crearTutor(tutor:Tutor):
    sql = """
    INSERT INTO tutores (nombre, telefono, direccion, dni)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql,(tutor.nombre, tutor.telefono, tutor.direccion, tutor.dni))
    conexion.commit()

def editarTutor(tutor:Tutor, id:int):
    sql = """
    UPDATE tutores
    SET nombre = %s,
        telefono = %s,
        direccion = %s,
        dni = %s
    WHERE id = %s
    """
    cursor.execute(sql,(tutor.nombre, tutor.telefono, tutor.direccion, tutor.dni, id))
    conexion.commit()

def eliminaTutor(id:int):
    sql = """
    DELETE FROM tutores
    WHERE id = %s
    """
    cursor.execute(sql,(id,))
    conexion.commit()