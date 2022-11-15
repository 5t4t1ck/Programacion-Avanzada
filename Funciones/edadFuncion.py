"""
Crear una función que permita conocer el rango de edad
de una persona
"""
nombre = input("Ingrese su nombre: ")
edad = int(input("Por favor ingrese su edad: "))

def edadCalcular(int:edad):
    global edad, nombre
    if edad >= 18 and edad<= 65:
        print(nombre,"Es mayor de edad")
    elif edad >= 65:
        print(nombre, "Usted es parte de la 3era Edad")
    else:
        print(nombre,"Es menor de edad")

edadCalcular(edad)
