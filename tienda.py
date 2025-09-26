print("----- TIENDA / COTIZADOR SIMPLE ---")

print("Menú de opciones:")
print("1. Calcular el total con IVA")
print("2. Calcular el total con descuento + IVA")
print("3. Calcular el precio unitario dado un total y cantidad")
print("4. Salir")

opcion = input("Opción (1-4): ")

if opcion == "1":
    precio = float(input("Ingresa el precio: $"))
    cantidad = float(input("Ingresa la cantidad: "))
    subtotal = precio*cantidad
    iva = (precio*cantidad)*0.16
    total = subtotal + iva
    print("Subtotal: $%.2f" %subtotal)
    print("IVA: $%.2f" %iva)
    print("Total: $%.2f" %total)
elif opcion == "2":
    precio = float(input("Ingresa el precio: $"))
    cantidad = int(input("Ingresa la cantidad: "))
    opc = input("Escribe tu código de descuento: ")
    if opc == "VERANO":
        descuento = 0.10
    elif opc == "SALDOS":
        descuento = 0.35
    elif opc == "BBVA":
        descuento = 0.05
    elif opc == "BANORTE25":
        descuento = 0.25
    else: 
        print("ERROR: Cupón no válido o no vigente")
    subtotal = (precio*cantidad)*(1-descuento)
    iva = subtotal*0.16
    total = subtotal + iva
    print("Subtotal (con descuento aplicado): $%.2f" %subtotal)
    print("IVA: $%.2f" %iva)
    print("Total: $%.2f" %total)
elif opcion == "3":
    total = float(input("Ingresa el total: $"))
    cantidad = int(input("Ingresa la cantidad: "))
    precioUnitario = total/cantidad
    print("PrecioUnitario: $%.2f" %precioUnitario)
else:
    print("ERROR: Opción seleccionada no válida")