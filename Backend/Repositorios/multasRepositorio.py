from database import cursor, conexion
from Modelos.multas import Multa
from datetime import datetime

def buscarMultaId(id:int):
    sql = """
    SELECT 
        m.*,
        t.nombreTutor AS nombreTutor,
        t.direccion AS direccion,
        t.telefono AS telefono,
        p.nombrePerro AS nombrePerro
    FROM multas m
    JOIN tutores t ON m.tutorid = t.id
    JOIN perros p ON m.perroid = p.id
    WHERE m.id = %s
    """
    cursor.execute(sql,(id,))
    return cursor.fetchone()

def obtenerMultas(anio: int = None, mes: int = None, dia: int = None, hora: int = None, estado: str = None):    
    sql = """
    SELECT 
        m.*,
        t.nombreTutor AS nombreTutor
    FROM multas m
    JOIN tutores t ON m.tutorid = t.id
    """
    condiciones = []
    valores = []

    if anio is not None:
        condiciones.append("EXTRACT(YEAR FROM fechahora) = %s")
        valores.append(anio)
    if mes is not None:
        condiciones.append("EXTRACT(MONTH FROM fechahora) = %s")
        valores.append(mes)
    if dia is not None:
        condiciones.append("EXTRACT(DAY FROM fechahora) = %s")
        valores.append(dia)
    if hora is not None:
        condiciones.append("EXTRACT(HOUR FROM fechahora) = %s")
        valores.append(hora)
    if estado is not None:
        condiciones.append("estado = %s")
        valores.append(estado)

    if condiciones:
        sql += " WHERE " + " AND ".join(condiciones)

    cursor.execute(sql, tuple(valores))
    return cursor.fetchall()


def obtenerMultasPerro(id:int):
    sql = """
    SELECT * FROM multas
    WHERE perroid = %s
    """
    cursor.execute(sql,(id,))
    return cursor.fetchall()

def obtenerMultasTutor(id:int):
    sql = """
    SELECT 
        m.*,
        p.nombrePerro AS nombrePerro
    FROM multas m
    JOIN perros p ON m.perroid = p.id
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

