print("----- CONVERSOR DE UNIDADES ---")

print("Menú de opciones:")
print("1. Temperatura: Celsius -> Fahrenheit")
print("2. Temperatura: Fahrenheit -> Celsius")
print("3. Longitud: Metros -> Centímetros")
print("4. Longitud: Centímetros -> Metros")
print("5. Kilogramos -> Gramos")
print("6. Gramos -> Kilogramos")
print("7. Salir")

opcion = input("Opción (1-7): ")

if opcion == "1":
    tCelsius = float(input("Ingresa la temperatura (°C): "))
    tFahrenheit = (tCelsius*1.8) + 32
    print("Temperatura (°F): %.3f" %tFahrenheit)
elif opcion == "2":
    tFahrenheit = float(input("Ingresa la temperatura (°F): "))
    tCelsius = (tFahrenheit - 32) / 1.8
    print("Temperatura (°C): %.3f" %tCelsius)
elif opcion == "3":
    lMetros = float(input("Ingresa la longitud (m): "))
    lCentimetros = lMetros *  100
    print("Longitud (cm): %.3f" %lCentimetros)
elif opcion == "4":
    lCentimetros = float(input("Ingresa la longitud (cm): "))
    lMetros = lCentimetros / 100
    print("Longitud (m): %.3f" %lMetros)
elif opcion == "5":
    mKilogramos = float(input("Ingresa la masa (kg): "))
    mGramos = mKilogramos * 1000
    print("Masa (g): %.3f" %mGramos)
elif opcion == "6":
    mGramos = float(input("Ingresa la masa (g): "))
    mKilogramos = mGramos / 1000
    print("Masa (kg): %.3f" %mKilogramos)
elif opcion == "7":
    print("Ejecución finalizada. ¡ADIÓS!")
else:
    print("ERROR: Opción seleccionada no válida")