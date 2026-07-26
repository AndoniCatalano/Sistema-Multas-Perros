def totalMultasTutor(id: int):
    multas = obtenerMultasTutor(id)
    total = sum(multa["monto"] for multa in multas)
    return total

def totalMultasPerro(id: int):
    multas = obtenerMultasPerro(id)
    total = sum(multa["monto"] for multa in multas)
    return total