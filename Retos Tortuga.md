# **Tarea 2 - Ejercicios Unidad 1**
## Reto 1 Simulación básica con print() e input()
### Descripción del reto

Este primer reto busca recrear movimientos simples de la tortuga, pero únicamente usando print() e input(). La idea es que el usuario ingrese valores y el programa muestre un rastro en texto que represente esos desplazamientos.

### **Lo que aprendí en este reto**
Comprendí cómo funciona la idea de “simular” algo sin hacerlo gráficamente.
Reforcé el uso de variables para guardar distancias y direcciones.
Aprendí que incluso con herramientas básicas como print() e input(), puedo representar movimientos si pienso en ellos de manera lógica.
Fue un buen primer paso para entender cómo turtle dibuja, todo se resume en mover una posición y mostrar ese cambio.

### **Código** 
``` Python
print("Simulador de tortuga en texto")  # Título del programa

pasos = int(input("¿Cuántos pasos quieres que avance la tortuga? "))   # Solicitar al usuario el número de pasos

print("Creando una tortuga simulada que da" ,pasos, "pasos...")  # Indicar la acción que se va a realizar
print("-" * pasos + ">") # Dibujar la tortuga en texto con la cantidad de pasos especificada
```

## Reto 2 Simulación de la tortuga bajando con print() e input()
### Descripción del reto

Aquí el objetivo fue simular el movimiento vertical hacia abajo. En lugar de un trazo horizontal, ahora la tortuga debía “bajar” y dejar una línea vertical en texto, igualmente tambien usando únicamente print() e input().
### Lo que aprendí en este reto
Profundicé en cómo representar posiciones verticales usando saltos de línea. Entendí mejor cómo separar el movimiento horizontal del vertical.
Vi que pequeños cambios en la lógica permiten dibujar direcciones diferentes, igual que en turtle.
Empecé a visualizar cómo más adelante estos movimientos se convertirán en funciones reutilizables.

### Código
``` Python
print("Simulador de tortuga en texto")  # Título del programa

pasos = int(input("¿Cuántos pasos quieres que avance la tortuga? "))   # Solicitar al usuario el número de pasos

print("Creando una tortuga simulada que da" ,pasos, "pasos...")  # Indicar la acción que se va a realizar
for _ in range(pasos):  # Dibujar la tortuga en texto con la cantidad de pasos especificada
    print("|")  
print("∨") # Dibujar la tortuga en texto con la cantidad de pasos especificada
```

## Reto 3 Girar y dibujar usando solo print() e input()
### Descripción del reto

En este reto simulé que la tortuga avanza hacia adelante y luego “gira” hacia abajo, representando el movimiento únicamente con texto.
La idea fue mostrar un trazo horizontal seguido de una línea vertical, como si la tortuga cambiara de dirección.
No utilicé condicionales ni lógica de orientación, simplemente tomé los valores del usuario y dibujé el desplazamiento en dos fases. primero horizontal y luego vertical.

### Lo que aprendí en este reto

Reforcé cómo transformar valores ingresados por el usuario en un dibujo hecho solo con caracteres.
Aprendí a combinar un tramo horizontal con uno vertical usando espacios, repeticiones y saltos de línea.
Entendí cómo simular un “giro” sin programar giros reales: basta con cambiar la forma de imprimir el trazo.
Confirmé que con print(), multiplicación de cadenas y un ciclo for puedo representar movimientos más complejos que un simple avance.

### Codigo
``` Python
print("Simulador de tortuga en texto")  # Título del programa

pasos1 = int(input("¿Cuántos pasos quieres que avance la tortuga? "))   # 1. Solicitar al usuario el número de pasos hacia adelante
pasos2 = int(input("¿Cuántos pasos quieres que baje la tortuga? "))   # 2. Solicitar al usuario el número de pasos hacia abajo


print("Creando una tortuga simulada que da" ,pasos1, "pasos hacia adelante, y luego da" ,pasos2, "pasos hacia abajo")  # Indicar la acción que se va a realizar
print("-" * pasos1 + ">") # 1. Dibujar la tortuga en texto con la cantidad de pasos especificada hacia adelante


for _ in range(pasos2):  #
    print(" " * pasos1 + "|") # 2. Dibujar la tortuga en texto con la cantidad de pasos especificada hacia abajo

print(" " * pasos1 + "v") # 2.1. Dibujar la tortuga en texto con la cantidad de pasos especificada hacia abajo
```

## Reto 4 Encapsular movimientos en funciones

### Descripción del reto
Reescribir los retos anteriores usando funciones como avanzar(), bajar(), girar(), etc.
Cada función representa una acción independiente de la tortuga.

### Lo que aprendí en este reto

- Entendí el poder de las funciones para organizar el código.
- Aprendí a separar la lógica en partes pequeñas y reutilizables, tal como haría una biblioteca real.
- Vi cómo cambia un programa cuando deja de ser un conjunto de prints y se convierte en un mini-sistema de funciones.

### Codigo
``` Python
print("Mi Tortuga Reto 4 - Funciones")
pos_x = 0 # Variable global para la posición horizontal de la tortuga

def adelante(pasos): # Función para mover la tortuga hacia adelante
    global pos_x  # Indica que usaremos la variable global pos_x
    print("-" * pasos + ">")  # Imprime la línea horizontal con la flecha
    pos_x = pasos   # Guarda la posición horizontal final

def abajo(pasos):  # Función para mover la tortuga hacia abajo
    # Imprime n líneas de bajada, alineadas con pos_x
    for _ in range(pasos): 
        print(" " * pos_x + "|") #
    print(" " * pos_x + "v")  # última línea es la flecha hacia abajo

# Programa principal
adelante(5) 
abajo(3)
```

## Reto 5 La tortuga baja escaleras
### Descripción del reto
Aquí la tortuga debe bajar escaleras, avanzar horizontalmente, luego bajar verticalmente, y repetir.
Lo clave es que la posición horizontal acumulada se mantenga correctamente.

## Lo que aprendí en este reto

Reforcé la lógica de coordenadas (aunque sea solo simbólica).
Entendí cómo combinar varios movimientos dentro de una sola función o proceso.
Vi cómo la acumulación de estado (posición) es esencial en simulaciones, igual que en turtle.
Este reto me enseñó a pensar paso a paso en la lógica detrás de un dibujo, no solo en los print().

## Código
``` Python
print ("reto 5 tortuga")
pos_x = 0  # posición horizontal acumulada (columna donde termina la flecha '>')

def adelante(pasos): # Función para mover la tortuga hacia adelante
    global pos_x  # usamos la variable global pos_x
    # dibuja la línea horizontal desplazada por pos_x
    print(" " * pos_x + "-" * pasos + ">")
 
    pos_x += pasos  # actualiza la posición horizontal

def abajo(pasos): # Función para mover la tortuga hacia abajo
  
    for _ in range(pasos): 
        print(" " * pos_x + "|")  # dibuja las líneas verticales desplazadas por pos_x
    print(" " * pos_x + "v")  

adelante(4)
abajo(2)

adelante(5)
abajo(3)

adelante(3)
abajo(4)
```

## Conclusión
Esta actividad me permitió entender mejor cómo se construyen y organizan los movimientos dentro de un programa, incluso cuando se trabaja únicamente con texto. A través de los retos fui identificando cómo representar acciones, cómo dividir un problema en pasos más pequeños y cómo convertir ideas en soluciones funcionales.

También reforcé el uso de entradas del usuario, ciclos, funciones y la forma en que cada parte del código puede aportar a un comportamiento más completo. En general, fue un ejercicio que me ayudó a pensar de manera más lógica y estructurada, y a ver cómo decisiones simples en el código pueden generar resultados visuales coherentes.

Finalizo esta actividad con una comprensión más clara de cómo diseñar comportamientos paso a paso y con más confianza para seguir construyendo soluciones cada vez más organizadas.

