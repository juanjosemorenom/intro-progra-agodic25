from random import choice
from time import sleep
from os import system

#-----FUNCIÓN: CONFIGURAR TABLERO--------------------------------------------------------------

def configurarTablero(): 

    a11 = 1
    a12 = 2
    a13 = 3
    a21 = 4
    a22 = 5
    a23 = 6
    a31 = 7
    a32 = 8
    a33 = 9 

    tablero = [
    [a11, a12, a13],
    [a21, a22, a23], 
    [a31, a32, a33]
    ] 

    return tablero

#-----FUNCIÓN: IMPRIMIR TABLERO----------------------------------------------------------------

def imprimirTablero(tablero):
            
    print(f"""      
        {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}
        ---------
        {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}
        ---------
        {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}  
    """) 

#-----FUNCIÓN: VERIFICAR PARIDAD--------------------------------------------------------------

def  verificarParidad(contadorTurno):
    paridad = contadorTurno % 2 
    if paridad == 0:
        return True
    else:
        return False

#-----FUNCIÓN: LEER CASILLA-------------------------------------------------------------------

def leerCasilla():
    while True:
        try:
            casilla = int(input(f"Ingresa un número del 1 al 9 para marcar la casilla correspondiente: "))
            if ((casilla >= 1) and (casilla <= 9)):
                return casilla
            else:
                print("ERROR: Índice de casilla no válido") 
        except ValueError:
            print("ERROR: Valor no válido. Intenta de nuevo") 

#----- FUNCIÓN: MARCAR CASILLA----------------------------------------------------------------

def marcarCasilla(tablero, casilla, sim, marcados, bandera):

    if casilla in marcados:
        print("ERROR: Casilla ya marcada. Inténtalo otra vez")
        bandera = 1
        return tablero, marcados, False
    
    tablero_actualizado = tablero[:][:]

    if casilla == 1 and bandera == 0:
        tablero_actualizado[0][0] = sim
    elif casilla == 2 and bandera == 0:
        tablero_actualizado[0][1] = sim
    elif casilla == 3 and bandera == 0:
        tablero_actualizado[0][2] = sim
    elif casilla == 4 and bandera == 0:
        tablero_actualizado[1][0] = sim
    elif casilla == 5 and bandera == 0:
        tablero_actualizado[1][1] = sim
    elif casilla == 6 and bandera == 0:
        tablero_actualizado[1][2] = sim
    elif casilla == 7 and bandera == 0:
        tablero_actualizado[2][0] = sim
    elif casilla == 8 and bandera == 0:
        tablero_actualizado[2][1] = sim
    elif casilla == 9 and bandera == 0:
        tablero_actualizado[2][2] = sim

    marcados_actualizado = marcados.copy()
    marcados_actualizado.add(casilla)

    return tablero_actualizado, marcados_actualizado, True

#-----FUNCIÓN: MOSTRAR RESULTADO--------------------------------------------------------------

def mostrarResultado(tablero, opc, turno, marcados):

    if (tablero[0][0] == tablero[0][1] == tablero[0][2]) or (tablero[1][0] == tablero[1][1] == tablero[1][2]) or (tablero[2][0] == tablero[2][1] == tablero[2][2]) or (tablero[0][0] == tablero[1][0] == tablero[2][0]) or (tablero[0][1] == tablero[1][1] == tablero[2][1]) or (tablero[0][2] == tablero[1][2] == tablero[2][2]) or (tablero[0][0] == tablero[1][1] == tablero[2][2]) or (tablero[0][2] == tablero[1][1] == tablero[2][0]):

        imprimirTablero(tablero)

        if opc == '1':
            print(f"\n¡FELICIDADES! Has ganado jugador {turno}\n")
        else:
            if turno % 2 == 0:
                print(f"\n¡PERDISTE! Ha ganado la CPU\n")
            elif turno % 2 == 1:
                print(f"\n¡FELICIDADES! Has ganado\n") 
        return True

    elif marcados == {1,2,3,4,5,6,7,8,9}: 
        imprimirTablero(tablero)
        print(f"\n¡EMPATE! El juego ha terminado\n")
        return True
    
    return False

#-----FUNCIÓN: JUEGAR CONTRA OTRO JUGADOR-----------------------------------------------------

def juegoOtroJugador(opc):

    tablero = configurarTablero()
    contadorTurno = 0
    marcados = set([])

    while True:

        bandera = 0
        contadorTurno = contadorTurno + 1

        imprimirTablero(tablero)     

        if verificarParidad(contadorTurno):
            turno = 2
            sim = 'O'
        else :
            turno = 1
            sim = 'X'
        print(f"Turno: JUGADOR {turno}\n")    

        casilla = leerCasilla()   
        tablero, marcados, success = marcarCasilla(tablero, casilla, sim, marcados, bandera)
        
        if not success:
            continue

        if mostrarResultado(tablero, opc, turno, marcados):
            break

#-----FUNCIÓN: JUEGAR CONTRA CPU--------------------------------------------------------------

def juegoCPU(opc):

    tablero = configurarTablero()
    contadorTurno = 0
    restantes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    marcados = set([])  

    while True:

        bandera = 0
        contadorTurno = contadorTurno + 1

        imprimirTablero(tablero)  

        if verificarParidad(contadorTurno) == True:
            turno = 2
            print(f"Turno: CPU\n")
            sim = 'O'  
            casilla = choice(restantes)
        else:
            turno = 1
            sim = 'X'
            casilla = leerCasilla() 

        tablero, marcados, success = marcarCasilla(tablero, casilla, sim, marcados, bandera)
        
        if not success:
            continue

        if casilla in restantes:
            restantes.remove(casilla)
        
        if mostrarResultado(tablero, opc, turno, marcados):
            break

def juegoGato():

    print("---¡Bienvenido al asistente de juego del Tic Tac Toe!---\n")

    while True:

        opc = input("¿Deseas jugar contra otro jugador, contra la CPU o salir (1: Contra otro jugador, 2: Contra la CPU, Otro: Salir)?\n")

        if opc == '1':
            juegoOtroJugador(opc)
            sleep(2)
            system("clear")
        elif opc == '2':
            juegoCPU(opc)
            sleep(2)
            system("clear")
        else: 
            sleep(2)
            system("clear")
            print("¡Adiós!\n")
            break

juegoGato()