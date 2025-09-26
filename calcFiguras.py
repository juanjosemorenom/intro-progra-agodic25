# from math import * #Nos importamos toda la librería
# from math import sqrt, pi #aquí importamos la función de raíz cuadrada y el valor de pi
from math import pi #importamos solo el valor de la constante pi

print("----- Bienvenidos a mi Calculadora de Figuras ---")
print("Menú de figuras:")
print("1. Cubo")
print("2. Prisma")
print("3. Pirámide")
print("4. Cilindro")
print("5. Cono")
print("6. Esfera")

figura = input("Figura (1-6): ")

print("-°-°-°- Menú de opciones -°-°-°-")
print("1. Calcular el área")
print("2. Calcular el volumen")
print("3. Calcular ambos")
print("4. Salir")

opcion = input("Opción (1-4): ")

if opcion == "1":
    if figura == "1": #Este if anidado controla la figura calcular el área.
        lado = float(input("Lado (cm): "))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2}")
    elif figura == "2":
        altura = float(input("Altura (cm): "))
        areaBase = float(input("Área de la base (cm): "))
        carasLaterales = float(input("Número de caras laterales: "))        
        areaPrisma = 2*areaBase + carasLaterales*altura
        print(f"El área del prisma es: {areaPrisma:.2}")
    elif figura == "3":
        pass
    elif figura == "4":
        pass
    elif figura == "5":
        pass
    elif figura == "6":
        pass
    else:
        print("No conozco esa figura.")
elif opcion == "2":
    if figura == "1": #Este if anidado controla la figura calcular el volumen.
        lado = float(input("Lado (cm): "))
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.2}")
    elif figura == "2":
        altura = float(input("Altura (cm): "))
        areaBase = float(input("Área de la base (cm): "))       
        volumenPrisma = areaBase*altura
        print(f"El volumen del prisma es: {volumenPrisma:.2}")
    elif figura == "3":
        pass
    elif figura == "4":
        pass
    elif figura == "5":
        pass
    elif figura == "6":
        pass
    else:
        print("No conozco esa figura.")
elif opcion == "3":
    if figura == "1": ##Este if anidado controla la figura calcular ambos.
        lado = float(input("Lado (cm): "))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2}")
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.2}")
    elif figura == "2":
        altura = float(input("Altura (cm): "))
        areaBase = float(input("Área de la base (cm): "))
        carasLaterales = float(input("Número de caras laterales: "))        
        areaPrisma = 2*areaBase + carasLaterales*altura
        print(f"El área del prisma es: {areaPrisma:.2}")     
        volumenPrisma = areaBase*altura
        print(f"El volumen del prisma es: {volumenPrisma:.2}")
    elif figura == "3":
        pass
    elif figura == "4":
        pass
    elif figura == "5":
        pass
    elif figura == "6":
        pass
    else:
        print("No conozco esa figura.")
elif opcion == "4":
    print("Hasta luego =)")
else:
    print("No conozco esa figura.")