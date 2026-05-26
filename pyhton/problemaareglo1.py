#Problema 6: Una pizzería desea desarrollar una aplicación para
#automatizar el proceso de ventas en el año 2026. La pizzería ofrece 5
#tipos de pizza, cada una con un tamaño y precio específico, según la
#siguiente información,Tipo Tamaño Porciones Precio
"""1 Pequeña (2 porciones) $10.000
2 Mediana (4 porciones) $15.000
3 Larga (6 porciones) $20.000
4 Familiar (8 porciones) $25.000
5 Extra Familiar (12 porciones) $35.000"""
#Requisitos del programa
"""1. El sistema debe permitir atender a un número X de clientes.
2. Cada cliente puede comprar varios tipos de pizza en una
misma orden.
- Por ejemplo: un cliente elige Pequeña (tipo 1), Larga (tipo 3) y
Familiar (tipo 4).
El precio total será $55.000 y el número total de porciones será
16.
3. Al finalizar todas las ventas, el programa debe mostrar:
- Cantidad total de pizzas vendidas por tipo.
- Valor total de las ventas.
- Número total de porciones vendidas.
Al finalizar, el sistema debe mostrar los siguientes resultados:
- Cantidad de pizzas vendidas por tipo.
- Precio total de las pizzas vendidas.
- El número total de porciones vendidas.
La pizzería usa una base de datos basada en Arreglos de la siguiente
forma:"""
#variables:
pizza_pequeña = 0
pizza_mediana = 0
pizza_larga = 0
pizza_familiar = 0
pizza_extra = 0
porciones_pequeña = 2
porciones_mediana = 4
porciones_larga = 6
porciones_familiar = 8
porciones_extra = 12
#ingresamos un input que pida la cantidad de clientes:
n = int(input("\n ingrese aqui el numero de clientes: "))
for i in range(n):
    print("Pizzeria la cebolla: ")
    print("eliga el numero de pizza con el numero entero:1,2,3,4 o 5: ")
    print("1: pizza pequeña (2 porciones)por: $10.000")
    print("2: pizza mediana (4porciones) por: $15.000")
    print("3: pizza larga (6 porciones) por: $20.000")
    print("4: pizza familia (8 porciones) por: $25.000")
    print("5: pizza extra familiar (12 porciones) por: $35.000 ")
    tipo_pizza = int(input("\n ingrese aqui el primer tipo de pizza que quiera: "))
    if tipo_pizza == 1:
        pizza_pequeña += 1
        pizza_pequeña = 10000
        porciones_pequeña += 1
    elif tipo_pizza == 2:
        pizza_mediana += 1
        pizza_mediana = 15000
        porciones_mediana += 1
    elif tipo_pizza == 3:
        pizza_larga += 1
        pizza_larga = 20000
        porciones_larga += 1
    elif tipo_pizza == 4:
        pizza_familiar += 1
        pizza_familiar = 25000
        porciones_familiar += 1
    elif tipo_pizza == 5:
        pizza_extra +=1
        pizza_extra = 35000
        porciones_extra += 1
    else:
        print("¡el valor introducido es incorrecto!")
    elegir_pizza = int(input("\n ¿Quiere agregar otra pizza?: si:1 , no:2 "))
    if elegir_pizza == 1:
        
            print("Pizzeria la cebolla: ")
            print("eliga el numero de pizza con el numero entero:1,2,3,4 o 5: ")
            print("1: pizza pequeña (2 porciones)por: $10.000")
            print("2: pizza mediana (4porciones) por: $15.000")
            print("3: pizza larga (6 porciones) por: $20.000")
            print("4: pizza familia (8 porciones) por: $25.000")
            print("5: pizza extra familiar (12 porciones) por: $35.000 ")
            tipo_pizza = int(input("\n ingrese aqui el primer tipo de pizza que quiera: "))
            if tipo_pizza == 1:
                pizza_pequeña += 1
                pizza_pequeña = 10000
                porciones_pequeña += 1
            elif tipo_pizza == 2:
                pizza_mediana += 1
                pizza_mediana = 15000
                porciones_mediana += 1
            elif tipo_pizza == 3:
                pizza_larga += 1
                pizza_larga = 20000
                porciones_larga += 1
            elif tipo_pizza == 4:
                pizza_familiar += 1
                pizza_familiar = 25000
                porciones_familiar += 1
            elif tipo_pizza == 5:
                pizza_extra +=1
                pizza_extra = 35000
                porciones_extra += 1
            else:
                print("¡el valor introducido es incorrecto!")
    elif elegir_pizza == 2:
        continue      


    
