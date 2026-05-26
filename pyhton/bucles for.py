"""
bucles con fro 
iterar sobre algo xd
"""
print("\n imprimir un bucle for" )
#lista
frutas = ["manzana","mandarina","toronja","fresa","piña"] 
for frutas in frutas:
    print(frutas)


#cadena iterable
cadena = "ssapo perro"
for caracter in cadena:
    print(caracter)

#para enumerar:
frutas = ["manzana","mandarina","toronja","fresa","piña"] 
for index,frutas in enumerate(frutas):
    print(f"el indice es {index} y la furta es {frutas}")

#continue:
print("\n continue" )
animales = ["perro","gato","loro","caiman","cocodrilo"]
for idx,animal in enumerate(animales):
    if animal == "loro":
        continue
    print(animal)

#comprencion en mayusculas:
animales = ["perro","gato","loro","caiman","cocodrilo"]
animales_mayus =[animal.upper() for animal in animales]
print(animales_mayus)






#bucles anidados:
#letras = ["a","b","c","d"]
#numero = [1,2,3,4]
#for letras in letra:
 #   for numeros in numero:
  #    print(f"{letras}{numero}")
         

