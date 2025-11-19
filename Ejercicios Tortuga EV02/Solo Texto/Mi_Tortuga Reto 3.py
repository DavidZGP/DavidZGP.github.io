print("Simulador de tortuga en texto")  # Título del programa

pasos1 = int(input("¿Cuántos pasos quieres que avance la tortuga? "))   # 1. Solicitar al usuario el número de pasos hacia adelante
pasos2 = int(input("¿Cuántos pasos quieres que baje la tortuga? "))   # 2. Solicitar al usuario el número de pasos hacia abajo


print("Creando una tortuga simulada que da" ,pasos1, "pasos hacia adelante, y luego da" ,pasos2, "pasos hacia abajo")  # Indicar la acción que se va a realizar
print("-" * pasos1 + ">") # 1. Dibujar la tortuga en texto con la cantidad de pasos especificada hacia adelante


for _ in range(pasos2):  #
    print(" " * pasos1 + "|") # 2. Dibujar la tortuga en texto con la cantidad de pasos especificada hacia abajo

print(" " * pasos1 + "v") # 2.1. Dibujar la tortuga en texto con la cantidad de pasos especificada hacia abajo