from random import choice

print("---¡Bienvenido al asistente de juego del Tic Tac Toe!---\n")

while True:

    opc = input("¿Deseas jugar contra otro jugador, contra la CPU o salir (1: Contra otro jugador, 2: Contra la CPU 3: Salir)?\n")

    if opc == '1':

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

        contadorTurno = 0
        marcados = set([])
        
        while True:

            bandera = 0
            contadorTurno += 1

            print(f"""      
                {a11} | {a12} | {a13}
                ---------
                {a21} | {a22} | {a23}
                ---------
                {a31} | {a32} | {a33}  
            """)

            if contadorTurno % 2 == 0:
                turno = 2
                sim = 'O'
            else:
                turno = 1
                sim = 'X'

            print(f"Turno: JUGADOR {turno}\n")
            casilla = int(input(f"Ingresa un número del 1 al 9 para marcar la casilla correspondiente: "))

            if casilla in marcados:
                bandera = 1

            if casilla == 1 and bandera == 0:
                a11 = sim
            elif casilla == 2 and bandera == 0:
                a12 = sim
            elif casilla == 3 and bandera == 0:
                a13 = sim
            elif casilla == 4 and bandera == 0:
                a21 = sim
            elif casilla == 5 and bandera == 0:
                a22 = sim
            elif casilla == 6 and bandera == 0:
                a23 = sim
            elif casilla == 7 and bandera == 0:
                a31 = sim
            elif casilla == 8 and bandera == 0:
                a32 = sim
            elif casilla == 9 and bandera == 0:
                a33 = sim
            else:
                print("ERROR: Valor ingresado no válido")
                contadorTurno -= 1
                continue

            marcados.add(casilla)

            if (a11 == a12 == a13) or (a21 == a22 == a23) or (a31 == a32 == a33) or (a11 == a21 == a31) or (a12 == a22 == a32) or (a13 == a23 == a33) or (a11 == a22 == a33) or (a13 == a22 == a31):
                print(f"""      
                {a11} | {a12} | {a13}
                ---------
                {a21} | {a22} | {a23}
                ---------
                {a31} | {a32} | {a33}  
                """)   
                print(f"\n¡FELICIDADES! Has ganado jugador {turno}\n")
                break
            
            elif marcados == {1,2,3,4,5,6,7,8,9}: 
                print(f"""      
                {a11} | {a12} | {a13}
                ---------
                {a21} | {a22} | {a23}
                ---------
                {a31} | {a32} | {a33}  
                """)  
                print(f"\n¡EMPATE! El juego ha terminado\n")
                break

    elif opc == '2':

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

        contadorTurno = 0
        restantes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        marcados = set([])
        
        while True:

            bandera = 0
            contadorTurno += 1

            print(f"""      
                {a11} | {a12} | {a13}
                ---------
                {a21} | {a22} | {a23}
                ---------
                {a31} | {a32} | {a33}  
            """)

            if contadorTurno % 2 == 0:
                turno = 2
                print(f"Turno: CPU\n")
                sim = 'O'
                casilla = choice(restantes)
                
            else:
                turno = 1
                print(f"Turno: JUGADOR\n")
                sim = 'X'
                casilla = int(input(f"Ingresa un número del 1 al 9 para marcar la casilla correspondiente: "))

            if casilla in marcados:
                bandera = 1

            if casilla == 1 and bandera == 0:
                a11 = sim
            elif casilla == 2 and bandera == 0:
                a12 = sim
            elif casilla == 3 and bandera == 0:
                a13 = sim
            elif casilla == 4 and bandera == 0:
                a21 = sim
            elif casilla == 5 and bandera == 0:
                a22 = sim
            elif casilla == 6 and bandera == 0:
                a23 = sim
            elif casilla == 7 and bandera == 0:
                a31 = sim
            elif casilla == 8 and bandera == 0:
                a32 = sim
            elif casilla == 9 and bandera == 0:
                a33 = sim
            else:
                print("ERROR: Valor ingresado no válido")
                contadorTurno -= 1
                continue

            marcados.add(casilla)
            restantes.remove(casilla)

            if (a11 == a12 == a13) or (a21 == a22 == a23) or (a31 == a32 == a33) or (a11 == a21 == a31) or (a12 == a22 == a32) or (a13 == a23 == a33) or (a11 == a22 == a33) or (a13 == a22 == a31):
                print(f"""      
                {a11} | {a12} | {a13}
                ---------
                {a21} | {a22} | {a23}
                ---------
                {a31} | {a32} | {a33}  
                """)   
                if turno % 2 == 0:
                    print(f"\n¡PERDISTE! Ha ganado la CPU\n")
                    break
                elif turno % 2 == 1:
                    print(f"\n¡FELICIDADES! Has ganado\n")
                    break
            
            elif marcados == {1,2,3,4,5,6,7,8,9}: 
                print(f"""      
                {a11} | {a12} | {a13}
                ---------
                {a21} | {a22} | {a23}
                ---------
                {a31} | {a32} | {a33}  
                """)  
                print(f"\n¡EMPATE! El juego ha terminado\n")
                break

    else: 
        print("¡Adiós!\n")
        break
