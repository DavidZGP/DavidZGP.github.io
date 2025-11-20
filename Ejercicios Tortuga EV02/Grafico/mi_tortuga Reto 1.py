import turtle
Pasos= int(input("Ingrese el número de pasos que desea que avance la tortuga: ")) # Solicitar al usuario el número de pasos
t = turtle.Turtle()   # Crea una tortuga
print("la tortuga avanzará", Pasos, "pasos")  # Indicar la acción que se va a realizar
t.forward(Pasos)        # Avanza las Unidades indicadas por el usuario
turtle.done()         # Mantiene la ventana abierta