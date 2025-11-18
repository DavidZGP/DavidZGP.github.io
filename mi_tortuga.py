import turtle
Pasos= int(input("Ingrese el número de pasos que desea que avance la tortuga: "))
t = turtle.Turtle()   # Crea una tortuga
print("la tortuga avanzará", Pasos, "pasos")
t.forward(Pasos)        # Avanza 100 unidades
turtle.done()         # Mantiene la ventana abierta