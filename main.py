from funciones import *
from variables import *
import time
from copy import deepcopy

tablero_usuario = tablero_aleatorio(tablero_vacio)
tablero_maquina = tablero_aleatorio(tablero_vacio)
tablero_maquina_oculto = deepcopy(tablero_vacio)

print("╔══════════════════════════════╗")
print("║                              ║")
print("║    ¡Bienvenido a Hundir la   ║")
print("║           Flota!             ║")
print("║                              ║")
print("╚══════════════════════════════╝")

time.sleep(1)
#Poder salir cuando quieras, instrucciones de juego, Jugar
while salir == False:

    print("""\n\n¡Bienvenido al juego Hundir la Flota! El objetivo es hundir
los barcos de tu oponente antes de que él hunda los tuyos.\n¡Que gane el mejor!\n
Para ver las instrucciones del juego introduce - 1\n
Para jugar una partida introduce - 2\n
Para salir del juego introduce - 3\n""")

    time.sleep(1)

    opcion = input("Introduce una opción: ").strip()

    if opcion == "1":
        print("""\nEl juego consiste en hundir la flota del contrincante. Para ello, hay que elegir
un tablero aleatorio de forma estratégica y encontrar y hundir con los disparos la flota contraria.
Juegas contra la máquina que dispara de forma automática y veras su tablero oculto.
Los barcos se colocan de forma aleatoria en posición horizontal o vertical:\n
- 1 barco que ocupa 4 cuadrados.
- 2 barcos de tres cuadros
- 3 barcos de 2 cuadros
- 4 barcos de un solo cuadro\n
Cada jugador dispone de un turno de disparo que se irá alternando. Para hacerlo dirá las
coordenadas. Por ejemplo “B3”, significa que su disparo corresponde a la casilla que se
encuentra en esa coordenada.\n
- Si la casilla está en blanco, responderá “agua”.
- Si en la casilla se encuentra parte de un barco responderá “tocado”. En ese caso
el jugador tiene derecho a un nuevo disparo en el mismo turno.\n
Si los tiros son “agua”, se marcará con una "o" la cuadrícula; si los disparos son “tocado”,
se marcará con una "x". De esta forma el jugador puede saber las cuadrículas que
quedan en blanco y en las que ya ha disparado.\n
Finalmente, gana el jugador que antes consigue hundir la flota del otro.\n""")

        time.sleep(1.5)

    elif opcion == "2":

        tablero_usuario = tablero_aleatorio(tablero_vacio)
        tablero_maquina = tablero_aleatorio(tablero_vacio)
        tablero_maquina_oculto = deepcopy(tablero_vacio)

        print("TABLERO USUARIO")
        pintar_tablero(tablero_usuario)
        cambiar = input("Introduce 'cambiar' si prefieres otro tablero, sino pulsa ENTER: ").lower().strip()
        while cambiar == "cambiar":
            tablero_usuario = tablero_aleatorio(tablero_vacio)
            pintar_tablero(tablero_usuario)
            cambiar = input("Introduce 'cambiar' si prefieres otro tablero, sino pulsa ENTER: ").lower().strip()
        print("TABLERO MÁQUINA")
        pintar_tablero(tablero_maquina_oculto)

        print("""Elige nivel de dificultad:\n\n
Fácil - 1\n
Medio - 2\n
Difícil - 3\n""")
        dificultad_correcto = False
        while dificultad_correcto == False:
            try:
                dificultad = int(input("Introduce una opción: ").strip())
                if dificultad > 0 and dificultad < 4:
                    dificultad_correcto = True
                else:
                    print("Introduce 1, 2 o 3")
            except:
                    print("Introduce 1, 2 o 3")

        fin_juego = False
        while fin_juego == False:
            turno_jugador = True
            turno_maquina = True
            while turno_jugador == True:
                
                print("Tu Turno!")
                time.sleep(0.5)

                i, j, l = pedir_coordenadas()

                if i == "salir":
                    turno_jugador = False
                    fin_juego = True
                    turno_maquina = False

                elif coordenadas_repetidas(i, j, tablero_maquina) == True:
                    print("Ya habías introducido esas coordenadas")

                elif disparo_acertado(i, j, tablero_maquina) == True:
                    tablero_maquina_oculto[i][j] = "x"
                    tablero_maquina[i][j] = "x"
                    print("Tocado en posición " + str(l) + str(j+1))
                    time.sleep(0.5)
                    vidas_maquina -= 1
                    if vidas_maquina == 0:
                        fin_juego = True
                        turno_jugador = False
                        print("Has Ganado!!")
                    else:
                        print("Vuelves a disparar")
                        time.sleep(0.5)
                        pintar_tablero(tablero_maquina_oculto)

                elif disparo_agua(i, j, tablero_maquina) == True:
                    tablero_maquina_oculto[i][j] = "o"
                    tablero_maquina[i][j] = "o"
                    print("Agua en " + str(l) + str(j+1))
                    turno_jugador = False
                    pintar_tablero(tablero_maquina_oculto)

                else:
                    print("Error desconocido")
                    break

            time.sleep(1.5)
            if vidas_maquina > 0:
                #Para dificultad 2 y 3
                c = 3
                #Para dificultad 3
                d = False
                while turno_maquina == True:

                    if dificultad == 1 or dificultad == 2:
                        i = coordenadas_maquina()
                        l = alfabeto[i]
                        j = coordenadas_maquina()
                    #Para dificultad 3
                    if dificultad == 3:
                        if d == False:
                            i = coordenadas_maquina()
                            l = alfabeto[i]
                            j = coordenadas_maquina()
                        else:
                            
                            if i != 9 and tablero_usuario[i+1][j] != "o" and tablero_usuario[i+1][j] != "x":
                                i += 1
                            
                            elif i != 1 and tablero_usuario[i-1][j] != "o" and tablero_usuario[i-1][j] != "x":
                                i -= 1
                            
                            elif j != 9 and tablero_usuario[i][j+1] != "o" and tablero_usuario[i][j+1] != "x":
                                j += 1
                            
                            elif j != 1 and tablero_usuario[i][j-1] != "o" and tablero_usuario[i][j-1] != "x":
                                j -= 1

                            else:
                                d = False

                            l = alfabeto[i]

                    if coordenadas_repetidas(i, j, tablero_usuario) == True:
                        pass

                    elif disparo_acertado(i, j, tablero_usuario) == True:
                        tablero_usuario[i][j] = "x"
                        print("Turno de la máquina!")
                        time.sleep(0.5)
                        print("Tocado en posición " + str(l) + str(j+1))
                        time.sleep(0.5)
                        print("La máquina vuelve a disparar")
                        vidas_jugador -= 1
                        time.sleep(0.5)
                        pintar_tablero(tablero_usuario)

                        if dificultad == 3:
                            d = True

                    elif disparo_agua(i, j, tablero_usuario) == True:

                        if dificultad == 1 or (dificultad == 3 and d == True):
                            tablero_usuario[i][j] = "o"
                            print("Turno de la máquina!")
                            time.sleep(0.5)
                            print("Agua en " + str(l) + str(j+1))
                            turno_maquina = False

                        #Tiene 3 intentos para acertar
                        elif dificultad == 2 or (dificultad == 3 and d == False):
                            c -= 1
                            if c == 0:
                                tablero_usuario[i][j] = "o"
                                print("Turno de la máquina!")
                                time.sleep(0.5)
                                print("Agua en " + str(l) + str(j+1))
                                turno_maquina = False

                    else:
                        print("Error desconocido")
                        break
                time.sleep(1.5)

            print("TABLERO USUARIO")
            pintar_tablero(tablero_usuario)
            print("TABLERO MÁQUINA")
            pintar_tablero(tablero_maquina_oculto)
            if vidas_jugador == 0:
                fin_juego = True
                print("Lo siento, la máquina ha Ganado")

    elif opcion == "3":
        salir = True

    else:
        print("Introduce una opción valida")
        time.sleep(1.5)
        