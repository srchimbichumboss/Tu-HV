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
pizza_pequeña = 10000
pizza_mediana = 15000
pizza_larga = 20000
pizza_familiar = 25000
pizza_extra = 35000
porciones_pequeña = 2
porciones_mediana = 4
porciones_larga = 6
porciones_familiar = 8
porciones_extra = 12
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
    tipo_pizza = int(input("\n ingrese aqui el primer tipo de pizza que quiera: "))
    if tipo_pizza == 1:
        total_ventas += pizza_pequeña
        porciones_ventas += porciones_pequeña
        contador_pequeña += 1
        total_ventas_dia += pizza_pequeña
        total_porciones_dia = pizza_pequeña
        total_pizzas_dia = contador_pequeña
        venta_cliente = pizza_pequeña
        porciones_cliente = porciones_pequeña
    elif tipo_pizza == 2:
        total_ventas += pizza_mediana
        porciones_ventas += porciones_mediana
        contador_mediana += 1
        total_ventas_dia += pizza_mediana
        total_porciones_dia = porciones_mediana
        total_pizzas_dia = contador_mediana
        venta_cliente = pizza_mediana
        porciones_cliente = porciones_mediana
    elif tipo_pizza == 3:
        total_ventas += pizza_larga
        porciones_ventas += porciones_larga
        contador_larga += 1
        total_ventas_dia += pizza_larga
        total_porciones_dia = pizza_larga
        total_pizzas_dia = contador_larga
        venta_cliente = pizza_larga
        porciones_cliente = porciones_larga
    elif tipo_pizza == 4:
        total_ventas += pizza_familiar
        porciones_ventas += porciones_familiar
        contador_familiar += 1
        total_ventas_dia += pizza_familiar
        total_porciones_dia = pizza_familiar
        total_pizzas_dia = contador_familiar
        venta_cliente = pizza_familiar
        porciones_cliente = porciones_familiar
    elif tipo_pizza == 5:
        total_ventas += pizza_extra
        porciones_ventas += porciones_extra
        contador_extra += 1
        total_ventas_dia += pizza_extra
        total_porciones_dia = pizza_extra
        total_pizzas_dia = contador_extra
        venta_cliente = pizza_extra
        porciones_cliente = porciones_extra
    else:
        print("¡el valor introducido es incorrecto!")


# --- SEGUNDA PIZZA (TU LÓGICA ORIGINAL) ---
    elegir_pizza = int(input("\n ¿Quiere agregar otra pizza?: si:1 , no:2 "))
    
    if elegir_pizza == 1:
        print("\n--- Agregando adicional ---")
        tipo_pizza = int(input("Ingrese el número de la segunda pizza: "))
        
        if tipo_pizza == 1:
            total_ventas += pizza_pequeña
            porciones_ventas += porciones_pequeña
            contador_pequeña += 1
            total_ventas_dia += pizza_pequeña
            total_porciones_dia = pizza_pequeña
            total_pizzas_dia = contador_pequeña
            venta_cliente = pizza_pequeña
            porciones_cliente = porciones_pequeña
    elif     tipo_pizza == 2:
            total_ventas += pizza_mediana
            porciones_ventas += porciones_mediana
            contador_mediana += 1
            total_ventas_dia += pizza_mediana
            total_porciones_dia = porciones_mediana
            total_pizzas_dia = contador_mediana
            venta_cliente = pizza_mediana
            porciones_cliente = porciones_mediana
    elif     tipo_pizza == 3:
            total_ventas += pizza_larga
            porciones_ventas += porciones_larga
            contador_larga += 1
            total_ventas_dia += pizza_larga
            total_porciones_dia = pizza_larga
            total_pizzas_dia = contador_larga
            venta_cliente = pizza_larga
            porciones_cliente = porciones_larga
    elif     tipo_pizza == 4:
            total_ventas += pizza_familiar
            porciones_ventas += porciones_familiar
            contador_familiar += 1
            total_ventas_dia += pizza_familiar
            total_porciones_dia = pizza_familiar
            total_pizzas_dia = contador_familiar
            venta_cliente = pizza_familiar
            porciones_cliente = porciones_familiar
    elif     tipo_pizza == 5:
            total_ventas += pizza_extra
            porciones_ventas += porciones_extra
            contador_extra += 1
            total_ventas_dia += pizza_extra
            total_porciones_dia = pizza_extra
            total_pizzas_dia = contador_extra
            venta_cliente = pizza_extra
            porciones_cliente = porciones_extra
    else:
            print("¡el valor introducido es incorrecto!")
        
else:
        print("¡el valor introducido es incorrecto!")
#---------------------variables por cliente-----------------------
#valor de la venta total:
print("------------------------factura cliente-------------------------------")
print(f"el valor total es:",{venta_cliente})
#total porciones vendidas:
print(f"el total de porciones es:",{porciones_cliente})
#contador pizzas:
print(f"la cantidad total de pizzas por categoria es:",{contador_pequeña})
print(f"la cantidad total de pizzas por categoria es:",{contador_mediana})
print(f"la cantidad total de pizzas por categoria es:",{contador_larga})
print(f"la cantidad total de pizzas por categoria es:",{contador_familiar})
print(f"la cantidad total de pizzas por categoria es:",{contador_extra})
#-------------------------------variables totales-----------------
print("----------------------------TOTALES------------------------------------")
print("======================================================================")
#valor de la venta total:
print(f"el valor total es:",{total_ventas_dia})
#total porciones vendidas:
print(f"el total de porciones es:",{total_porciones_dia})
#contador pizzas:
print(f"la cantidad total de pizzas por categoria es:",{total_pizzas_dia})
