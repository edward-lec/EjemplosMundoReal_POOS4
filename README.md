# Introducción
La Programación Orientada a Objetos (POO) es un paradigma de programación que permite modelar problemas del mundo real mediante el uso de clases y objetos, facilitando la organización, reutilización y mantenimiento del código. En este trabajo se desarrolló un ejemplo práctico de POO en Python, aplicando sus principios fundamentales a través de una situación real: la gestión de un hotel y sus habitaciones. El objetivo principal fue demostrar el uso correcto de clases, atributos, métodos e interacción entre objetos, siguiendo una estructura clara y buenas prácticas de programación.
# 2. Desarrollo
Para el desarrollo del proyecto se creó un directorio llamado EjemplosMundoReal_POO, dentro del repositorio de Programación Orientada a Objetos. En este directorio se implementó un sistema básico que simula la administración de un hotel.
# 2.1 Estructura del proyecto
El proyecto está compuesto por los siguientes archivos:
•	habitacion.py: contiene la definición de la clase Habitacion.
•	hotel.py: contiene la definición de la clase Hotel.
•	main.py: archivo principal que permite la ejecución y prueba del sistema.
# 2.2 Clase Habitacion
La clase Habitacion representa una habitación dentro de un hotel. En ella se definen atributos que describen sus características y métodos que permiten gestionar su estado. Esta clase modela un objeto del mundo real de forma sencilla y clara.
# 2.3 Clase Hotel
La clase Hotel representa la entidad principal del sistema. Sus principales características son:
•	Posee atributos como el nombre del hotel y una lista de habitaciones.
•	Incluye métodos que permiten agregar y administrar habitaciones.
•	Mantiene una relación directa con la clase Habitacion, demostrando la interacción entre objetos.
Esta clase cumple el rol de gestor del sistema, centralizando la lógica principal del programa.
# 2.4 Archivo main.py
El archivo main.py se encarga de crear instancias de las clases y ejecutar el programa. Desde este archivo se prueban los métodos definidos, permitiendo verificar el correcto funcionamiento del sistema y la interacción entre las clases.
# 2.5 Principios de POO aplicados
Durante el desarrollo del proyecto se aplicaron los siguientes principios de la Programación Orientada a Objetos:
•	Encapsulación: cada clase contiene sus propios atributos y métodos.
•	Abstracción: se representan entidades reales (hotel y habitación) mediante clases.
•	Modularidad: el programa se divide en archivos independientes, facilitando su mantenimiento.
•	Interacción entre objetos: el hotel administra objetos de tipo habitación.
Además, el código fue comentado de manera clara para facilitar su comprensión.
# 3. Conclusiones
El desarrollo de este proyecto permitió comprender y aplicar de forma práctica los conceptos fundamentales de la Programación Orientada a Objetos en Python. La modelación de un sistema de hotel demostró cómo las clases y objetos pueden representar situaciones reales de manera ordenada y eficiente.
De esta manera, se logró una correcta organización del código mediante la separación de responsabilidades en distintos archivos, lo cual mejora la legibilidad y escalabilidad del programa.
# 4. Control de versiones
Durante el desarrollo del proyecto se utilizó Git para el control de versiones, realizando commits con mensajes descriptivos y sincronizando los cambios con el repositorio en GitHub, garantizando un correcto seguimiento del avance del trabajo.
