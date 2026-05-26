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
"""--------------MODIFICADO-----------------"""
##variables:
#pizza_pequeña = 10000
#pizza_mediana = 15000
#pizza_larga = 20000
#pizza_familiar = 25000
#pizza_extra = 35000
#porciones:
#porciones_pequeña = 2
#porciones_mediana = 4
#porciones_larga = 6
#porciones_familiar = 8
#porciones_extra = 12
"""----------PRECIOS PIZZAS--------"""
#nuevas variables:
precios_pizzas = [10000,15000,20000,25000,35000]
porciones_pizzas = [2,4,6,8,12]
facturas = []
precio_cliente = []
porciones_cliente = []
"""-------variables sin cambiar-----"""
total_ventas = 0
porciones_ventas = 0
contador_pequeña = 0
contador_mediana = 0
contador_larga = 0
contador_familiar = 0
contador_extra = 0
total_ventas_dia = 0
total_porciones_dia = 0
total_pizzas_dia = 0
venta_cliente = 0
porciones_cliente = 0
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
    eleccion_usuario = int(input("\n ingrese aqui el primer tipo de pizza que quiera: "))
#mensaje de arreglo:
    if eleccion_usuario >= 6:
        print("-----!!!!!el numero digitado no es correcto!!!!!----")
#pizza pequeña:
    indice = eleccion_usuario - 1
    precio = precios_pizzas [0]
    precio_cliente = precios_pizzas [0]
    porciones = porciones_pizzas [0]
    porciones_cliente = porciones_pizzas [0]

#pizza mediana:
    indice = eleccion_usuario - 2
    precio = precios_pizzas [1]
    precio_cliente = precios_pizzas [1]
    porciones = porciones_pizzas  [1]
    porciones_cliente = porciones_pizzas [1]

#pizza larga:
    indice = eleccion_usuario - 3
    precio = precios_pizzas [2]
    precio_cliente = precios_pizzas [2]
    porciones = porciones_pizzas  [2]
    porciones_cliente = porciones_pizzas [2]

#pizza familiar:
    indice = eleccion_usuario - 4
    precio = precios_pizzas [3]
    precio_cliente = precios_pizzas [3]
    porciones = porciones_pizzas  [3]
    porciones_cliente = porciones_pizzas [3]

#pizza extra:
    indice = eleccion_usuario - 5
    precio = precios_pizzas [4]
    precio_cliente = precios_pizzas [4]
    porciones = porciones_pizzas  [4]
    porciones_cliente = porciones_pizzas [4]


    pizza_adicional = int(input("\n ¿Quiere agregar otra pizza?: si:1 , no:2 "))
    if pizza_adicional ==2:
        print("\n Preparando la cuenta")
        continue
    if pizza_adicional == 1:
        print("\n--- Agregando adicional ---")
        eleccion_usuario = int(input("Ingrese el número de la segunda pizza: "))
    elif eleccion_usuario >= 6:
        print("-----!!!!!el numero digitado no es correcto!!!!!----")
#pizza pequeña:
    indice = eleccion_usuario - 1
    precio = precios_pizzas [0]
    precio_cliente = precios_pizzas [0]
    porciones = porciones_pizzas [0]
    porciones_cliente = porciones_pizzas [0]

#pizza mediana:
    indice = eleccion_usuario - 2
    precio = precios_pizzas [1]
    precio_cliente = precios_pizzas [1]
    porciones = porciones_pizzas  [1]
    porciones_cliente = porciones_pizzas [1]

#pizza larga:
    indice = eleccion_usuario - 3
    precio = precios_pizzas [2]
    precio_cliente = precios_pizzas [2]
    porciones = porciones_pizzas  [2]
    porciones_cliente = porciones_pizzas [2]

#pizza familiar:
    indice = eleccion_usuario - 4
    precio = precios_pizzas [3]
    precio_cliente = precios_pizzas [3]
    porciones = porciones_pizzas  [3]
    porciones_cliente = porciones_pizzas [3]

#pizza extra:
    indice = eleccion_usuario - 5
    precio = precios_pizzas [4]
    precio_cliente = precios_pizzas [4]
    porciones = porciones_pizzas  [4]
    porciones_cliente = porciones_pizzas [4]

facturas.append([precio_cliente,porciones_cliente])


#---------------------variables por cliente-----------------------
#valor de la venta total:
print("------------------------factura cliente-------------------------------")
for i in facturas:
    contador = 1
    print(f"cliente:{contador} total:{i[0]}- porciones: {i[1]}")
    contador += 1
print("==========================TOTAL DIA============================")


    #print(porciones)
    #print(indice)

#print(f"el valor total es:",{venta_cliente})
##total porciones vendidas:
#print(f"el total de porciones es:",{porciones_cliente})
##contador pizzas:
#print(f"la cantidad total de pizzas por categoria es:",{contador_pequeña})
#print(f"la cantidad total de pizzas por categoria es:",{contador_mediana})
#print(f"la cantidad total de pizzas por categoria es:",{contador_larga})
#print(f"la cantidad total de pizzas por categoria es:",{contador_familiar})
#print(f"la cantidad total de pizzas por categoria es:",{contador_extra})
#
#
#
#
#
#
#
#
#
##-------------------------------variables totales-----------------
#print("----------------------------TOTALES------------------------------------")
#print("======================================================================")
##valor de la venta total:
#print(f"el valor total es:",{total_ventas_dia})
##total porciones vendidas:
#print(f"el total de porciones es:",{total_porciones_dia})
##contador pizzas:
#print(f"la cantidad total de pizzas por categoria es:",{total_pizzas_dia})
#