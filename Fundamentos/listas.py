
lista = []
print(lista) #Lista vacía.

lista.append(50)
lista.append("Loja")
lista.append(7.5)
print(lista) #Lista con datos.

lista1 =[]
lista1 = lista.copy()
print(lista1)
lista.clear()
print(lista) #Lista vacía
print(lista, lista1)

lista_vocales = ["a","e","e","i","o","u"]
print(lista_vocales.count("e"))
print(len(lista_vocales))

lista = [1, 2, 3]
print("Indice 0 =", lista[0])
print("Indice 1 =", lista[1])
print("Indice 2 =", lista[2])

lista = ["manzana","pera","banana"]
print(lista)
lista.pop()
print(lista)

lista = ["Juan", "Pedro", "María"]
print(lista)
lista.remove("Pedro")
print(lista)

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(lista)
lista.reverse()
print(lista)

lista = ["q","w","e","r","t","y","u","i","o","p","ñ","l","k","j","h","g","f","d","s","a","z","x","c","v","b","n","m"]
print(lista)
lista.sort()
print(lista)

#lista = ["c","C", 7.00] # Solo se puede con datos del mismo tipo
