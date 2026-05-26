"""
listas metodos
"""
import os
os.system("clear")

lista1 = [1,2,3,4,5,6,7,9,]
lista1.append(10)#añade algo a la lista.
print(lista1)
lista1.insert(1,'@')#inserta algo en ese indice que quieras ubicar.
print(lista1)
lista1.extend(['viva la arepa','Q',])#extiende pero se usa doble corchete
print(lista1)
#remover la primera cosa
lista1.remove("@")
print(lista1)
#eliminar el ultimo de la lista
ultimo = lista1.pop()
print(ultimo)
print(lista1)
#mas especifico
lista1.pop(0)
print(lista1)#elimina uno especifico
"""
eliminar 
"""
del lista1[-1]
print(lista1)#elimina la arepa.

"""
eliminar todo
"""
lista1.clear()
print(lista1)#literalmente elimina la lista
#eliminar por rango:
lista2 = [9,8,7,7,6,5,5,4,4,4,3,3,2,3,45,76]
del lista2[2:]
print(lista2)#elimina en un rango
"""
ordenar 
"""

lista3 = [1,2,34,4,5,6,7,8,7,6,54,5,6,776,7,7,8,8,7,6]
lista3.sort()
print(lista3)#organiza la lista.and
"""
esto la modifica y no la guarda
"""
#guardandola seria
sorted_numbers = [1,2,34,4,5,6,7,8,7,6,54,5,6,776,7,7,8,8,7,6]
numeros = lista3
lista3.sort()
print(sorted_numbers)
"""
cantidad de elemntos que aparece en una lista
"""
print(len(lista3))
print(lista3.count('7'))
