import turtle
Pasos= int(input("Ingrese el número de pasos que desea que avance la tortuga: "))  # Solicita al usuario el número de pasos
t = turtle.Turtle()   # Crea una tortuga
print("la tortuga avanzará", Pasos, "pasos")    # Indica los pasos que avanzará la tortuga
t.forward(Pasos)        # Avanza el numero de unidades deseado
t.right(90)             # Gira 90 grados a la derecha
t.forward(Pasos)       # Avanza el numero de unidades deseado
turtle.done()         # Mantiene la ventana abierta