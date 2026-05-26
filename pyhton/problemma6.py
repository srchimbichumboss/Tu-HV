#"""Problema 5: Una nueva tienda deportiva desea saber qué productos
#ofrecer para los hinchas de los equipos de fútbol colombianos. Para esto,
#se quiere preguntar a 10 fanáticos del futbol:"""
#- Cuál es su equipo favorito.
"""- Qué tipo de articulo deportivo prefiere entre camiseta, chaqueta,
gorra o morral con el logo de su equipo favorito.
- Edad del fanático del fútbol.
- Cantidad de días al año en los cuales asisten al estadio a partidos
de su equipo favorito."""
"""El programa debe mostrar:
- Cantidad de fanáticos por equipo de fútbol
- Promedio de edades de los hinchas por cada equipo de fútbol.
- El tipo de articulo deportivo preferido por los hinchas
- Promedio de días al año en los cuales los hinchas asisten al
estadio"""
#variables:
n = int(input("\n Ingrese la cantidad de hinchas a encuestar: "))
equipos_futbol = 0
equipo_m = 0
equipo_n = 0
equipo_j = 0
equipo_b = 0
equipo_med = 0
camisa = 0
chaqueta = 0
gorra = 0
morral = 0
edad_inchas_millonarios = 0
edad_inchas_nacional = 0
edad_inchas_junior = 0
edad_inchas_bucaramanga = 0
edad_inchas_medellin = 0

for i in range(n):
    print("Equipos de futbol:Millonarios: 1, Nacional:2 Junior:3, Bucaramanga:4, Medellin:5")
    equipos = int(input("\n Seleccione el numero de su equipo: "))
    if 1 == m:
        equipo_m = m
        edades_inchasm = int(input("\n Ingrese su edad: "))
    elif 2 == n:
        equipo_n = n
        edades_inchasn = int(input("\n Ingrese su edad: "))
    elif 3 == j:
        equipo_j = j
        edades_inchasj = int(input("\n Ingrese su edad: "))
    elif 4 == b:
        equipo_b = b
        edades_inchasb = int(input("\n Ingrese su edad: "))
    elif 5 == med:
        equipo_med = med
        edades_inchasmed = int(input("\n Ingrese su edad: "))
    
    print("Qué tipo de articulo deportivo prefiere entre camiseta:1, chaqueta:2, gorra:3, o morral:4 con su logo")
    articulos = int(input("\n ingrese aqui su producto preferido"))
    if 1 == c:
        camisa = c
    elif 2 == ch:
        chaqueta = ch
    elif 3 == g:
        gorra = g
    elif 4 == mo:
        morral = mo

    dia_estadio = int(input("\n Ingrese la cantidad de dias al año en que va al estadio: "))
#muchas variables sobre edades:
edad_inchas_millonarios = edades_inchasm / equipo_m
edad_inchas_nacional = edades_inchasn / equipo_n
edad_inchas_junior = edad_inchas_junior / equipo_j
edad_inchas_bucaramanga = edad_inchas_bucaramanga / equipo_b
edad_inchas_medellin = edad_inchas_medellin / equipo_med
#dias en el estadio(variable):
promedio_dias_estadio = dia_estadio / n
#salidas:numero de inchas
print(f"el numero de inchas de el equipo es:",{equipo_m})
print(f"el numero de inchas de el equipo es:",{equipo_n})
print(f"el numero de inchas de el equipo es:",{equipo_j})
print(f"el numero de inchas de el equipo es:",{equipo_b})
print(f"el numero de inchas de el equipo es:",{equipo_med})
#promedio edad inchas:
print(f"el promedio de edad de los inchas es: ",{edad_inchas_millonarios})
print(f"el promedio de edad de los inchas es: ",{edad_inchas_nacional})
print(f"el promedio de edad de los inchas es: ",{edad_inchas_junior})
print(f"el promedio de edad de los inchas es: ",{edad_inchas_bucaramanga})
print(f"el promedio de edad de los inchas es: ",{edad_inchas_medellin})
#articulo preferido por los inchas:
print(f"articulo personas: ",{camisa})
print(f"articulo personas: ",{chaqueta})
print(f"articulo personas: ",{gorra})
print(f"articulo personas: ",{morral})
#promedio de dias al año en el estadio:
print(f"el promedio de dias al año de los inchas es:", {promedio_dias_estadio})
