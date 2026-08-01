from database import cursor, conexion
from Modelos.perros import Perro

def buscarPerroId(id:int):
    sql = """
    SELECT 
        p.*,
        t.nombreTutor AS nombreTutor,
        t.direccion AS direccion,
        t.telefono AS telefono
    FROM perros AS p 
    JOIN tutores t ON p.tutorid = t.id
    WHERE id = %s
    """
    cursor.execute(sql,(id,))
    return cursor.fetchone()

def ObtenerPerros(edad:str = None, color: str = None, genero: str = None, nombre: str = None, raza: str = None):
    sql = """
    SELECT 
        p.*,
        t.nombreTutor AS nombreTutor
    FROM perros p 
    JOIN tutores t ON p.tutorid = t.id
    """
    condiciones = []
    valores = []

    if color:
        condiciones.append("color ILIKE %s")
        valores.append(f"%{color}%")
    if genero:
        condiciones.append("genero = %s")
        valores.append(genero)
    if nombre:
        condiciones.append("nombrePerro ILIKE %s")
        valores.append(f"%{nombre}%")
    if raza:
        condiciones.append("raza ILIKE %s")
        valores.append(f"%{raza}%")
    if edad:
        condiciones.append("edad = %s")
        valores.append(edad)

    if condiciones:
        sql += " WHERE " + " AND ".join(condiciones)

    cursor.execute(sql,(tuple(valores)))
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
     INSERT INTO perros (raza, genero, nombrePerro, edad, foto, tutorid)
     VALUES (%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(sql,(perro.raza, perro.genero, perro.nombre, perro.edad, perro.foto, perro.tutorid))
    conexion.commit()

def editarPerro(perro:Perro, id:int):
    sql = """
    UPDATE perros 
    SET raza = %s, 
        genero = %s,
        nombrePerro = %s,
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