print("----- GESTOR DE CALIFICACIONES ---")

print("Menú de opciones:")
print("1. Calcular promedio")
print("2. Calcular calificación final con ponderaciones")
print("3. Mostrar mayor y menor calificación")
print("4. Verificar si el alumno aprueba o reprueba")
print("5. Salir")

opcion = input("Opción (1-5): ")

if opcion == "1":
    print("Ingresa tus 3 calificaciones parciales: ")
    cal1 = float(input("Calificación 1: "))
    cal2 = float(input("Calificación 2: "))
    cal3 = float(input("Calificación 3: "))
    promedio = (cal1 + cal2 + cal3) / 3
    print("Tu promedio es: %.2f" %promedio)
elif opcion == "2":
    print("Ingresa tus 3 calificaciones parciales: ")
    cal1 = float(input("Calificación 1: "))
    cal2 = float(input("Calificación 2: "))
    cal3 = float(input("Calificación 3: "))
    print("Ingresa las 3 ponderaciones parciales en porcentaje: ")
    pond1 = float(input("Ponderación 1: "))
    pond2 = float(input("Ponderación 2: "))
    pond3 = float(input("Ponderación 3: "))  
    calPond = (cal1*(pond1/100)) + (cal2*(pond2/100)) + (cal3*(pond3/100))
    print("Tu calificación final ponderada es: %.2f" %calPond)
elif opcion == "3":
    print("Ingresa tus 3 calificaciones parciales: ")
    cal1 = float(input("Calificación 1: "))
    cal2 = float(input("Calificación 2: "))
    cal3 = float(input("Calificación 3: "))
    if (cal1 >= cal2 and cal1 >=cal3):
        mayor = cal1
    elif (cal2 >= cal1 and cal2 >=cal3):
        mayor = cal2
    else:
        mayor = cal3
    print("Tu calificación mayor es: %.2f" %mayor)
    if (cal1 <= cal2 and cal1 <=cal3):
        menor = cal1
    elif (cal2 <= cal1 and cal2 <=cal3):
        menor = cal2
    else:
        menor = cal3
    print("Tu calificación menor es: %.2f" %menor)
elif opcion == "4":
    cal1 = float(input("Calificación 1: "))
    cal2 = float(input("Calificación 2: "))
    cal3 = float(input("Calificación 3: "))
    print("Ingresa las 3 ponderaciones parciales en porcentaje: ")
    pond1 = float(input("Ponderación 1: "))
    pond2 = float(input("Ponderación 2: "))
    pond3 = float(input("Ponderación 3: "))  
    calPond = (cal1*(pond1/100)) + (cal2*(pond2/100)) + (cal3*(pond3/100))
    if calPond >= 6:
        print("HAS APROBADO :)")
    else:
        print("NO HAS APROBADO :(")
elif opcion == "5":
    print("Operación finalizada")
else:
    print("ERROR: Opción seleccionada no válida")