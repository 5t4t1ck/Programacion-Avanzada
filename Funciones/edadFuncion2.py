"""
Crear una función que permita conocer el rango de edad
de una persona
"""

def edadCalcular(edad, nombre):
    if edad >= 18 and edad<= 65:
        print("Es mayor de edad")
    elif edad >= 65:
        print("Usted es parte de la 3era Edad")
    else:
        print("Es menor de edad")

edadCalcular(12, "Juan")
