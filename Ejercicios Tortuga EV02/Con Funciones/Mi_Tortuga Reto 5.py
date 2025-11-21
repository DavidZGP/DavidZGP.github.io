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
