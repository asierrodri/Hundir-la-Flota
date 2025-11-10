from funciones import *
from variables import *
import time
from copy import deepcopy

tablero_usuario = tablero_aleatorio(tablero_vacio)
tablero_maquina = tablero_aleatorio(tablero_vacio)
tablero_maquina_oculto = deepcopy(tablero_vacio)

#Poder salir cuando quieras, instrucciones de juego, volver a jugar, Jugar
while salir == False:
    print("╔══════════════════════════════╗")
    print("║                              ║")
    print("║    ¡Bienvenido a Hundir la   ║")
    print("║           Flota!             ║")
    print("║                              ║")
    print("╚══════════════════════════════╝")

    time.sleep(1)

    print("""\n\n¡Bienvenido al juego Hundir la Flota! El objetivo es hundir
los barcos de tu oponente antes de que él hunda los tuyos.\n¡Que gane el mejor!\n
Para ver las instrucciones del juego introduce - 1\n
Para jugar una partida introduce - 2\n
Para salir del juego introduce - 3\n""")

    time.sleep(1)



    print("TABLERO USUARIO")
    pintar_tablero(tablero_usuario)
    print("TABLERO MÁQUINA")
    pintar_tablero(tablero_maquina_oculto)

    while fin_juego == False:
        turno_jugador = True
        turno_maquina = True
        while turno_jugador == True:
            
            print("Tu Turno!")
            time.sleep(0.5)
            #meter la coordenada en una misma variable del input
            i, j = pedir_coordenadas()

            if coordenadas_repetidas(i, j, tablero_maquina) == True:
                print("Ya habías introducido esas coordenadas")

            elif disparo_acertado(i, j, tablero_maquina) == True:
                tablero_maquina_oculto[i][j] = "x"
                tablero_maquina[i][j] = "x"
                #pintar bien la posicion
                print("Tocado en posición " + str(i) + "," + str(j))
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
                print("Agua")
                turno_jugador = False
                pintar_tablero(tablero_maquina_oculto)

            else:
                print("Error desconocido")
                break

        time.sleep(1.5)
        if vidas_maquina > 0:
            while turno_maquina == True:
                #Que no se repita cuando repite coordenada
                
                i = coordenadas_maquina()
                j = coordenadas_maquina()

                if coordenadas_repetidas(i, j, tablero_usuario) == True:
                    pass

                elif disparo_acertado(i, j, tablero_usuario) == True:
                    tablero_usuario[i][j] = "x"
                    print("Turno de la máquina!")
                    time.sleep(0.5)
                    print("Tocado en posición " + str(i) + "," + str(j))
                    time.sleep(0.5)
                    print("La máquina vuelve a disparar")
                    vidas_jugador -= 1
                    time.sleep(0.5)
                    pintar_tablero(tablero_usuario)

                elif disparo_agua(i, j, tablero_usuario) == True:
                    tablero_usuario[i][j] = "o"
                    print("Turno de la máquina!")
                    time.sleep(0.5)
                    print("Agua")
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