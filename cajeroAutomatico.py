print("----- CAJERO AUTOMÁTICO ---")

print("Menú de opciones:")
print("1. Consultar saldo")
print("2. Retirar")
print("3. Depositar")
print("4. Salir")

saldoInicial = float(input("Ingresa tu monto inicial: $"))

opcion = input("Opción (1-4): ")

if opcion == "1":
    print("Tu saldo actual es: $", saldoInicial)
elif opcion == "2":
    retiro = float(input("Ingresa tu monto a retirar: "))
    if retiro > saldoInicial:
        print("RETIRO NO EXITOSO: ")
        print("El saldo actual no es suficiente")
    else:
        saldoActual = saldoInicial - retiro
        print("RETIRO EXITOSO: ")
        print("El saldo actual es: $%.2f" %saldoActual)
elif opcion == "3":
    deposito = float(input("Ingresa tu monto a depositar: $"))
    saldoActual = saldoInicial + deposito
    print("DEPÓSITO EXITOSO: ")
    print("El saldo actual es: $%.2f" %saldoActual)
elif opcion == "4":
    print("OPERACIÓN FINALIZADA")
else:
    print("ERROR: Opción seleccionada no válida")