tupla = ("Hola mundo", "esto", "es", "una", "tupla")
print(type(tupla))

#tupla.append("Juan") No se puede modificar las tuplas
lista = list(tupla)
print(type(lista))

lista.append("Juan")
print(lista)
print(tupla)

tupla = ("a","a","b","c","d","e")
print(tupla.count("a"))
print(tupla.index("e"))

lista = (1, 2, 3, 4, 5)
print(lista[0])

tupla2 = tuple(lista)
print(type(tupla2))
print(type(lista))

primerValor = int("3")
segundoValor = str(3)

print(type(primerValor))
print(type(segundoValor))