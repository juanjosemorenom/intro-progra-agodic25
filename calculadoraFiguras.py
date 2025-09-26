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
        print(f"El área del cubo es: {areaCubo:.2} cm^2")
    elif figura == "2":
        altura = float(input("Altura (cm): "))
        areaBase = float(input("Área de la base (cm): "))
        carasLaterales = float(input("Número de caras laterales: "))        
        areaPrisma = 2*areaBase + carasLaterales*altura
        print(f"El área del prisma es: {areaPrisma:.2} cm^2")
    elif figura == "3":
        areaBase = float(input("Área de la base (cm): "))
        carasLaterales = float(input("Número de caras laterales: "))  
        apotema = float(input("Apotema (cm): "))      
        areaPiramide = areaBase + (carasLaterales*apotema)/2
        print(f"El área de la pirámide es: {areaPiramide:.2} cm^2")
    elif figura == "4":  
        radio = float(input("Radio (cm): "))
        altura = float(input("Altura (cm): "))      
        areaCilindro = 2 * pi * radio * (radio + altura)
        print(f"El área del cilindro es: {areaCilindro:.2} cm^2")       
    elif figura == "5":
        radio = float(input("Radio (cm): "))
        generatriz = float(input("Generatriz (cm): "))      
        areaCono = pi * radio * (radio + generatriz)
        print(f"El área del cono es: {areaCono:.2} cm^2") 
    elif figura == "6":
        radio = float(input("Radio (cm): "))    
        areaEsfera = 4 * pi * (radio**2)
        print(f"El área de la esfera es: {areaEsfera:.2} cm^2") 
    else:
        print("No conozco esa figura.")
elif opcion == "2":
    if figura == "1": #Este if anidado controla la figura calcular el volumen.
        lado = float(input("Lado (cm): "))
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.2} cm^3")
    elif figura == "2":
        altura = float(input("Altura (cm): "))
        areaBase = float(input("Área de la base (cm): "))       
        volumenPrisma = areaBase*altura
        print(f"El volumen del prisma es: {volumenPrisma:.2} cm^3")
    elif figura == "3":
        areaBase = float(input("Área de la base (cm): ")) 
        altura= float(input("Altura (cm): "))      
        volumenPiramide = (1/3) * areaBase * altura
        print(f"El volumen de la pirámide es: {volumenPiramide:.2} cm^3")
    elif figura == "4":
        radio = float(input("Radio (cm): "))
        altura = float(input("Altura (cm): "))      
        volumenCilindro = pi * (radio**2) *altura
        print(f"El volumen del cilindro es: {volumenCilindro:.2} cm^3")  
    elif figura == "5":
        radio = float(input("Radio (cm): "))
        altura= float(input("Altura (cm): "))      
        volumenCono = (1/3) * pi * (radio**2) * altura
        print(f"El volumen del cono es: {volumenCono:.2} cm^3") 
    elif figura == "6":
        radio = float(input("Radio (cm): "))    
        volumenEsfera = (4/3) * pi * (radio**3)
        print(f"El volumen de la esfera es: {volumenEsfera:.2} cm^3") 
    else:
        print("No conozco esa figura.")
elif opcion == "3":
    if figura == "1": ##Este if anidado controla la figura calcular ambos.
        lado = float(input("Lado (cm): "))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2} cm^2")
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.2} cm^3")
    elif figura == "2":
        altura = float(input("Altura (cm): "))
        areaBase = float(input("Área de la base (cm): "))
        carasLaterales = float(input("Número de caras laterales: "))        
        areaPrisma = 2*areaBase + carasLaterales*altura
        print(f"El área del prisma es: {areaPrisma:.2} cm^2")     
        volumenPrisma = areaBase*altura
        print(f"El volumen del prisma es: {volumenPrisma:.2} cm^3")
    elif figura == "3":
        areaBase = float(input("Área de la base (cm): "))
        carasLaterales = float(input("Número de caras laterales: "))  
        apotema = float(input("Apotema (cm): "))      
        areaPiramide = areaBase + (carasLaterales*apotema)/2
        print(f"El área de la pirámide es: {areaPiramide:.2} cm^2")
        altura= float(input("Altura (cm): "))      
        volumenPiramide = (1/3) * areaBase * altura
        print(f"El volumen de la pirámide es: {volumenPiramide:.2} cm^3")
    elif figura == "4":
        radio = float(input("Radio (cm): "))
        altura = float(input("Altura (cm): "))      
        areaCilindro = 2 * pi * radio * (radio + altura)
        print(f"El área del cilindro es: {areaCilindro:.2} cm^2")        
        volumenCilindro = pi * (radio**2) *altura
        print(f"El volumen del cilindro es: {volumenCilindro:.2} cm^3")  
    elif figura == "5":
        radio = float(input("Radio (cm): "))
        generatriz = float(input("Generatriz (cm): "))      
        areaCono = pi * radio * (radio + generatriz)
        print(f"El área del cono es: {areaCono:.2} cm^2")
        altura= float(input("Altura (cm): "))      
        volumenCono = (1/3) * pi * (radio**2) * altura
        print(f"El volumen del cono es: {volumenCono:.2} cm^3") 
    elif figura == "6":
        radio = float(input("Radio (cm): "))    
        areaEsfera = 4 * pi * (radio**2)
        print(f"El área de la esfera es: {areaEsfera:.2} cm^2")  
        volumenEsfera = (4/3) * pi * (radio**3)
        print(f"El volumen de la esfera es: {volumenEsfera:.2} cm^3") 
    else:
        print("No conozco esa figura.")
elif opcion == "4":
    print("Hasta luego =)")
else:
    print("No conozco esa figura.")
