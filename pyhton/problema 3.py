"""
Problema 3: Una tienda de café desea automatizar el registro de
ventas diarias. El administrador registra las ventas en tres momentos:
mañana, tarde y noche.
"""
#El programa debe:
#1. Solicitar el valor de las ventas en cada momento.
#2. Calcular el total de ventas del día.
#3. Comparar el total con la meta diaria de $150.000.
#Salida esperada:
#- Total vendido.
#- Mensaje:
#✓ “Meta alcanzada” si el total ≥ 150.000.
#✓ “Meta no alcanzada” si el total < 150.000.

"""entrada"""
valor_jornada_mañana = int(input("\n ingrese el total facturado en la jornada mañana:"))
valor_jornada_tarde = int(input("\n ingrese el total facturado en la jornada tarde:"))
valor_jornada_noche = int(input("\n ingrese el total facturado en la jornada noche:"))
total = valor_jornada_mañana + valor_jornada_tarde + valor_jornada_noche

#evaluar meta diaria:
total_dia = 150
#Salida
if total > 150:
    print("Meta alcanzada")
elif total < 150:
        print("Meta no alcanzada")

print("el total obtenido en las tres jornadas del dia es :",valor_jornada_mañana + valor_jornada_tarde + valor_jornada_noche)

"""
valor_jornada_mañana = int(input("\n ingrese el total facturado en la jornada mañana:"))
valor_jornada_tarde = int(input("\n ingrese el total facturado en la jornada tarde:"))
valor_jornada_noche = int(input("\n ingrese el total facturado en la jornada noche:"))
valor = [valor_jornada_mañana + valor_jornada_tarde + valor_jornada_noche]
#evaluar meta diaria:
total_dia = 150
#Salida
if valor > 150:
    print("Meta alcanzada")
elif valor < 150:
        print("Meta no alcanzada")

print("el total obtenido en las tres jornadas del dia es :",valor_jornada_mañana + valor_jornada_tarde + valor_jornada_noche)
"""