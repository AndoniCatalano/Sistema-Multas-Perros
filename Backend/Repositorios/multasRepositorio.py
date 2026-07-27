from database import cursor, conexion
from Modelos.multas import Multa
from datetime import datetime

def buscarMultaId(id:int):
    sql = """
    SELECT * FROM multas
    WHERE id = %s
    """
    cursor.execute(sql,(id,))
    return cursor.fetchone()

def ObtenerMultas(fechahora:datetime, estado:chr):
    sql = "SELECT * FROM multas"
    condiciones = []
    valores = []
    if fechahora:
        condiciones.append(" YEAR(fechahora) = %s")
        valores.append(fechahora.year)
        if hasattr(fechahora,'month') and fechahora.month:
            condiciones.append(" MONTH(fechahora) = %s")
            valores.append(fechahora.month)
            if hasattr(fechahora,'day') and fechahora.day:
                condiciones.append(" DAY(fechahora) = %s")
                valores.append(fechahora.day)
                if hasattr(fechahora,'hour') and fechahora.hour:
                    condiciones.append(" HOUR(fechahora) = %s")
                    valores.append(fechahora.hour)
    if estado:
        condiciones.append("estado = %s")
        valores.append(estado)
    if condiciones:
        sql += " WHERE " + " AND ".join(condiciones)

    cursor.execute(sql,tuple(valores))
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

