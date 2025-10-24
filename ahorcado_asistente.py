from random import choice
from time import sleep
from os import system

contadorRonda = 0

palabras = ["Rusia",
            "Canadá",
            "Estados_Unidos",
            "China",
            "Brasil",
            "Australia",
            "India",
            "Argentina",
            "Kazajistán",
            "Argelia"]

print("\n---¡Bienvenido al asistente del juego del Ahorcado!---")
print("Edición: PAÍSES MÁS EXTENSOS DEL MUNDO\n")
print("Tienes 3 vidas para adivinar el nombre del país\n ")

while True:

    contadorVidas = 3
    contadorRonda += 1
    print(f"RONDA: {contadorRonda}\n")

    palabra = choice(palabras)
    palabras.remove(palabra)
    tam = len(palabra)
    palabra = palabra.upper()
    pAdivinada = "_"*tam
    listaPalabra = list(palabra)
    listaAdivinada= list(pAdivinada)
    letrasAdivinadas = set()

    while contadorVidas > 0:

        print("".join(listaAdivinada))
        print("\n")
        print(f"Vidas restantes: {contadorVidas}")
        letra = input("Ingresa una letra: ").strip().upper()

        if letra == 'A':
            letraP = 'Á'
        if letra == 'E':
            letraP = 'É'
        elif letra == 'I':
            letraP = 'Í'
        elif letra == 'O':
            letraP = 'Ó'
        elif letra == 'U':
            letraP = 'Ú'

        if letra in listaPalabra or letraP in listaPalabra:
            print("¡Letra encontrada!\n")
            for i in range(tam):
                if listaPalabra[i] == letra:
                    listaAdivinada[i] = letra
                if listaPalabra[i] == letraP:
                    listaAdivinada[i] = letraP
        else:
            print("¡Letra no encontrada!\n")
            contadorVidas -= 1

        if "".join(listaAdivinada) == palabra:
            print("¡FELICIDADES! Has adivinado el nombre del país: \n")
            print("".join(listaAdivinada)+"\n")
            break
        elif contadorVidas == 0:
            print(f"¡PERDISTE! No has adivinado el nombre del país: {palabra}")
            break

    opc = input("¿Quieres jugar otra ronda?: 1: Sí , 2: No\n")
    if opc != '1':
        break

    if not palabras:
        print("Ya no quedan más palabras. Fin del juego.")
        break
