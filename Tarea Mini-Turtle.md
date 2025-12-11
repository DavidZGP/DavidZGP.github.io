# Tarea Mini-Turtle 🐢
Este proyecto hace parte de mi proceso de aprendizaje en Pensamiento Algorítmico y Programación en Python.
La actividad consiste en transformar un pequeño simulador de tortuga en texto en dos versiones:

## Versión Funcional – Paquete mini_turtle_task
En esta primera versión, convertí funciones sueltas en un paquete modular, aplicando buenas prácticas de organización de código en Python.
### Incluye:
- adelante(n): dibuja un movimiento horizontal.
- abajo(n): dibuja un movimiento vertical.
- reiniciar(): reinicia la posición horizontal.

Separación en módulos (drawer_logic.py, __init__.py)
un archivo main.py para pruebas.

Esta versión demuestra cómo crear un paquete simple y exponer una interfaz limpia para el usuario.

## Versión Orientada a Objetos – Paquete mini_turtle_oo_task

En esta versión refactoricé toda la lógica utilizando Programación Orientada a Objetos (POO).
El estado deja de ser global y pasa a ser parte de un objeto:

- *Clase Tortuga*

- self.posicion_x como atributo encapsulado

- Métodos: adelante(), abajo(), reiniciar()

Permite crear múltiples tortugas independientes y es con compatible con movimientos acumulados (escaleras)

Esta versión demuestra encapsulamiento, modularidad y creación de objetos con estados propios.

## Objetivo General

Aprender y aplicar:
- Modularidad y empaquetado en Python
- Buenas prácticas de diseño
- Conceptos fundamentales de POO
- Separación entre interfaz y lógica interna
- Gestión de repositorios y documentación

## Repositorios
- Versión funcional: [https://github.com/DavidZGP/Ejercicio-1-Version-Funcional-Modularidad]

- Versión orientada a objetos: [https://github.com/DavidZGP/Ejercicio-2-Version-Orientada-a-Objetos]


