print("----- Calculadora de Palabras ---")
print("Menú de opciones:")
print("1. Contar caracteres")
print("2. Pasar a MAYÚSCULAS")
print("3. Pasar a minúsculas")
print("4. Contar cuantas veces aparece una letra")
print("5. Reemplazar una letra por otra")
print("6. Unir cada letra con guiones")
print("7. Sumar la longitud de dos sentencias")
print("8. Salir")

texto = input("Ingresa una palabra o sentencia: ")
opcion = input("Elige una opción del menú (1-8): ")

if opcion == "1":
    #len --> length
    #Indentacion, es característica principal de Python
    #Nos indica que estas líneas dependen de la "línea padre"
    #La línea que está No indentada anterior
    #Esta línea es un comentario, por tanto no se ejecuta.
    conteoCaracteres = len(texto)
    print("Número de caracteres: "+str(len(texto)))
    # print("Número de caracteres:", conteoCaracteres)
    # print(f"Número de caracteres: {conteoCaracteres}")
    # print(f"Número de caracteres: {len(texto)}")
elif opcion == "2":
    # minusCadena = upper(texto)
    print("Cadena en mayúsculas: "+texto.upper())
elif opcion == "3":
    # minusCadena = lower(texto)
    print("Cadena en minúsculas: " +texto.lower())
elif opcion == "4":
    letra = input("Ingresa una letra")
    print(letra+ " aparece " +str(texto.find(letra))+ " veces en la cadena")
elif opcion == "5":
    letraAnt = input("Ingresa la letra que quieres cambiar: ")
    letraNue = input("Ingresa la letra por la que quieres cambiarla: ")
    print("Cadena con letra reemplazada:" +texto.replace(letraAnt, letraNue) )
elif opcion == "6":
    sepCad = "-".join(texto)
    print("Cadena separada: ", sepCad)
elif opcion == "7":
    texto2 = input("Ingresa otra palabra o sentencia: ")
    conteoCaracteres = len(texto)
    conteoCaracteres2 = len(texto2)
    int(conteoCaracteres)
    int(conteoCaracteres2)
    suma = conteoCaracteres + conteoCaracteres2
    print("Suma de caracteres de las dos sentencias: ", suma)
elif opcion == "8":
    print("Procesando...")
    print("Adiós :)")
    pass
else:
    print("Opción incorrecta, debes elegir una opción del Menú, ¡Adiós!")