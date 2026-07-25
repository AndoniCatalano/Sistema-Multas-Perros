from database import cursor, conexion
from Modelos.multas import Multa

def obtenerMultas():
    cursor.execute("SELECT * FROM multas")
    return cursor.fetchall()

def buscarMultaId(id:int):
    sql = """
    SELECT * FROM multas
    WHERE id = %s
    """
    cursor.execute(sql,(id,))
    return cursor.fetchone()

def obtenerMultasPerro(id:int):
    sql = """
    SELECT * FROM multas
    WHERE perroid = %s
    """
    cursor.execute(sql,(id,))
    return cursor.fetchall()

def obtenerMultasTutor(id:int):
    sql = """
    SELECT * FROM multas
    WHERE tutorid = %s
    """
    cursor.execute(sql,(id,))
    return cursor.fetchall()

def crearMulta(multa:Multa):
    sql = """
    INSERT INTO multas (monto, fechahora, perroid, tutorid, descripcion, estado)
    VALUES (%s, %s,%s,%s,%s,%s)
    """
    cursor.execute(sql,(multa.monto, multa.fechahora,multa.perroid,multa.tutorid,multa.descripcion,multa.estado))
    conexion.commit()

def editarMulta(multa:Multa, id:int):
    sql = """
    UPDATE multas
    SET monto = %s,
        fechahora = %s,
        perroid = %s,
        tutorid = %s,
        descripcion = %s,
        estado = %s
    WHERE id = %s
    """
    cursor.execute(sql,(multa.monto, multa.fechahora,multa.perroid,multa.tutorid,multa.descripcion,multa.estado, id))
    conexion.commit()

def eliminarMulta(id:int):
    sql = """
    DELETE FROM multas
    WHERE id = %s
    """
    cursor.execute(sql,(id,))
    conexion.commit()

def totalMultasTutor(id: int):
    multas = obtenerMultasTutor(id)
    total = sum(multa["monto"] for multa in multas)
    return total

def totalMultasPerro(id: int):
    multas = obtenerMultasPerro(id)
    total = sum(multa["monto"] for multa in multas)
    return total