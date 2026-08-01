# Documentación

## Descripción

Este proyecto consiste en una API REST para gestionar tutores, perros y multas. El objetivo es registrar infracciones cometidas por perros y asociar cada multa al tutor responsable.

## Modelo de datos

El sistema está compuesto por tres entidades:

- **Tutores:** almacenan la información de los dueños de los perros.
- **Perros:** contienen los datos de cada perro y una referencia a su tutor.
- **Multas:** registran las infracciones cometidas por un perro asociado a su vez a un tutor.

Las relaciones son:

- Un tutor puede tener varios perros.
- Un perro pertenece a un único tutor.
- Un perro puede tener varias multas.
- Cada multa pertenece a un solo perro y tutor.

## Funcionamiento

El flujo del sistema es el siguiente:

1. Se registra un tutor.
2. Se registra uno o más perros asociados al tutor.
3. Cuando un perro comete una infracción, se crea una multa.
4. La multa queda vinculada al perro y, por medio de esa relación, se puede identificar al tutor responsable.