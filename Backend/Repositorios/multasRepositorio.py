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

def editarEstadoMulta(estado:chr, id:int):
    sql = """
    UPDATE multas
    SET estado = %s
    WHERE id = %s
    """
    cursor.execute(sql,(estado, id))
    conexion.commit()

def eliminarMulta(id:int):
    sql = """
    DELETE FROM multas
    WHERE id = %s
    """
    cursor.execute(sql,(id,))
    conexion.commit()

