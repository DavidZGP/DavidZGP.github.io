# Variable global para recordar dónde termina la línea horizontal
pos_x = 0

def adelante(pasos): # Función para mover la tortuga hacia adelante
    global pos_x  # Indica que usaremos la variable global pos_x
    print("-" * pasos + ">")  # Imprime la línea horizontal con la flecha
    pos_x = pasos   # Guarda la posición horizontal final

def abajo(pasos):  # Función para mover la tortuga hacia abajo
    # Imprime n líneas de bajada, alineadas con pos_x
    for _ in range(pasos): 
        print(" " * pos_x + "|") #
    print(" " * pos_x + "v")  # última línea es la flecha hacia abajo


# -----------------------
# Ejemplo solicitado:
adelante(5) 
abajo(3)

