# DavidZGP.github.io
## **Páginas Personal — Proyectos y Aprendizajes en Python**

Este repositorio alberga mi página personal, donde comparto lo que he aprendido en clase sobre programación en Python. Aquí explico conceptos esenciales, muestro un ejemplo de código y ofrezco mi reflexión personal sobre el proceso. Además, incluyo el enlace a la versión publicada del sitio.

## **Lo que aprendí en clase**

Programa y algoritmo: Un programa es un conjunto de instrucciones para que la computadora lleve a cabo tareas paso a paso. Un algoritmo es la base lógica detrás de ese programa: la secuencia ordenada de pasos necesaria para resolver un problema.

Variables y tipos de datos: Trabajé con variables para almacenar y manipular información dentro del código. Aprendí sobre diferentes tipos de datos como números, cadenas de texto y valores booleanos (True / False).

Estructuras de control: Profundicé en sentencias condicionales (if) y ciclos (bucles), que son fundamentales para tomar decisiones o repetir acciones según lo que necesite ejecutar el programa.

## **Ejemplo de código**

Como parte de la página, incluí un fragmento de código en Python que ejemplifica algunos de los conceptos aprendidos (variables, condicionales, etc.). Esto le da a la página un enfoque práctico y aplicable.




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


## **Mi reflexión**

Al aprender estos fundamentos, me di cuenta de que la programación no es solo escribir líneas de código, sino pensar de forma lógica y estructurada. Resolver problemas implica planear soluciones, descomponer tareas en pasos claros y anticipar qué va a suceder en cada etapa. Este proceso ha fortalecido mi forma de razonar y me ha motivado a seguir explorando Python y el desarrollo de software en general.
