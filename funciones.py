#Pintar tableros
def pintar_tablero(tablero):
    from variables import alfabeto
    i = 1
    print("*", end = " ")
    while i<11:
        print(i, end=" ")
        i += 1
    print()
    x = 0
    for p in tablero:
        print(alfabeto[x], end=" ")
        for i in p:
            print(i, end=" ")
        print("|")
        x += 1
    print("- "*12)

#Pruebas con barcos fijos
def colocar_barcos_fijos(tablero):
    from copy import deepcopy
    tablero_con_barcos = deepcopy(tablero)
    tamano_barco = 4
    posicion = 0
    while tamano_barco:
        tablero_con_barcos[1][posicion] = "B"
        posicion += 1
        tamano_barco -= 1
    return tablero_con_barcos

#Colocar barcos aleatoriamente en tablero
def colocar_barco(letra, barco, tablero_con_barcos):
    import random
    cantidad_barco = barco.cantidad
    
    while cantidad_barco > 0:
        direccion = random.randint(0,1)
        tamano_barco = barco.tamano
        i = random.randint(0, 10-barco.tamano)
        j = random.randint(0, 10-barco.tamano)
        c = 0
        colocar = True
        if direccion == 0:
            while tamano_barco > 0:
                if tablero_con_barcos[i][j+c] != "·":
                    #Si no ponía las dos se quedaba colgado
                    colocar = False
                    break
                else:
                    c += 1
                    tamano_barco -= 1
            if colocar == True:
                tamano_barco = barco.tamano
                c = 0
                while tamano_barco > 0:
                    tablero_con_barcos[i][j+c] = letra
                    c += 1
                    tamano_barco -= 1
                cantidad_barco -= 1
                
        if direccion == 1:
            while tamano_barco > 0:
                if tablero_con_barcos[i+c][j] != "·":
                    colocar = False
                    break
                else:
                    c += 1
                    tamano_barco -= 1
            if colocar == True:
                tamano_barco = barco.tamano
                c = 0
                while tamano_barco > 0:
                    tablero_con_barcos[i+c][j] = letra
                    c += 1
                    tamano_barco -= 1
                cantidad_barco -= 1
    
#Crear el tablero aleatorio
def tablero_aleatorio(tablero):
    from clases import Barco
    from copy import deepcopy
    
    destructor = Barco(1, 4)
    submarino = Barco(2, 3)
    acorazado = Barco(3, 2)
    portaviones = Barco(4, 1)

    tablero_con_barcos = deepcopy(tablero)
    colocar_barco("d", destructor, tablero_con_barcos)
    colocar_barco("s", submarino, tablero_con_barcos)
    colocar_barco("a", acorazado, tablero_con_barcos)
    colocar_barco("p", portaviones, tablero_con_barcos)

    return tablero_con_barcos

#Coordenadas
def coordenada_letra_correcta(coordenada):
    if coordenada == "SALIR":
        return True
    elif len(coordenada) != 1:
        return False
    #Me funcionó y no se me ocurrió otra forma
    elif coordenada < "A" or coordenada > "J":
        return False
    else:
        return True
    
def coordenada_numero_correcto(coordenada):
    if coordenada < 1 or coordenada > 10:
        return False
    else:
        return True

def pedir_coordenadas():
    from variables import alfabeto

    i = ""
    l = ""
    j = 0
    while coordenada_letra_correcta(i) == False:
        i = input("Introduce la primera coordenada ALFABÉTICA o introduce SALIR: ").upper().strip()
    if i == "SALIR":
        i = "salir"
    else:
        l = i
        i = alfabeto.index(i)
    if i != "salir":
        while coordenada_numero_correcto(j) == False:
            try:
                j = int(input("Introduce la segunda coordenada NUMÉRICA: "))
            except:
                print("Introduce un número entre 1 y 10")
        j =int(j) - 1

    return i, j, l

def coordenadas_maquina():
    import random
    coordenada = random.randint(0, 9)
    return coordenada

#Disparos    
def disparo_acertado(i, j, tablero):
    if tablero[i][j] != "·":
        return True
    else:
        return False
    
def disparo_agua(i, j, tablero):
    if tablero[i][j] == "·":
        return True
    else:
        return False

def coordenadas_repetidas(i, j, tablero):
    if tablero[i][j] == "x" or tablero[i][j] == "o":
        return True
    else:
        return False
    