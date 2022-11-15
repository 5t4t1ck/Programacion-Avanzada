diccionario = { 
    "nombre":"Juan",
    "trabajo":"electricista",
    "edad":"35"
}

print(type(diccionario))
print(diccionario)

print(diccionario["nombre"])
print(diccionario["edad"])

print(diccionario.get("trabajo"))
diccionario["trabajo"] = "programador"
print(diccionario.get("trabajo"))
print(diccionario)
print(len(diccionario))
diccionario["Estado Civil"] = "Divorciado"
print(diccionario)
diccionario.pop("edad")
print(diccionario)
diccionario2 = diccionario.copy()
print(diccionario)
print(diccionario2)

del diccionario["nombre"]
print(diccionario)
diccionario.clear()
print(diccionario)
diccionario = diccionario2.copy()
print(diccionario)

perros = {
  "Tobby":{
    "name": "Tobby",
    "age": 6
    },
  "Leo":{
    "name": "Leo",
    "age": 1
    }
}
print(perros)

Tobby = {
    "name": "Tobby",
    "age": 6
    }
Leo = {
    "name": "Leo",
    "age": 1
    }
perros = {
  "Tobby": Tobby,
  "Leo":Leo
}
print(perros)

perritos = dict(name="Rocky", age=7)
print(perritos)