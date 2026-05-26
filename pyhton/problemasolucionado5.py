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
equipo_m = 0
equipo_n = 0
equipo_j = 0
equipo_b = 0
equipo_med = 0
camisa = 0
chaqueta = 0
gorra = 0
morral = 0
sum_edad_millonarios = 0
sum_edad_nacional = 0
sum_edad_junior = 0
sum_edad_bucaramanga = 0
sum_edad_medellin = 0
total_dias_estadio = 0

for i in range(n):
    print("Equipos de futbol: Millonarios: 1, Nacional: 2, Junior: 3, Bucaramanga: 4, Medellin: 5")
    equipos = int(input("\n Seleccione el numero de su equipo: "))
    if equipos == 1:
        equipo_m += 1
        edades_inchasm = int(input("\n Ingrese su edad: "))
        sum_edad_millonarios += edades_inchasm
    elif equipos == 2:
        equipo_n += 1
        edades_inchasn = int(input("\n Ingrese su edad: "))
        sum_edad_nacional += edades_inchasn
    elif equipos == 3:
        equipo_j += 1
        edades_inchasj = int(input("\n Ingrese su edad: "))
        sum_edad_junior += edades_inchasj
    elif equipos == 4:
        equipo_b += 1
        edades_inchasb = int(input("\n Ingrese su edad: "))
        sum_edad_bucaramanga += edades_inchasb
    elif equipos == 5:
        equipo_med += 1
        edades_inchasmed = int(input("\n Ingrese su edad: "))
        sum_edad_medellin += edades_inchasmed
    else:
        print("\n Opción de equipo no válida")
        continue

    print("Qué tipo de articulo deportivo prefiere entre camiseta:1, chaqueta:2, gorra:3, o morral:4 con su logo")
    articulos = int(input("\n ingrese aqui su producto preferido: "))
    if articulos == 1:
        camisa += 1
    elif articulos == 2:
        chaqueta += 1
    elif articulos == 3:
        gorra += 1
    elif articulos == 4:
        morral += 1
    else:
        print("\n Opción de articulo no válida")

    dia_estadio = int(input("\n Ingrese la cantidad de dias al año en que va al estadio: "))
    total_dias_estadio += dia_estadio

edad_inchas_millonarios = sum_edad_millonarios / equipo_m if equipo_m else 0
edad_inchas_nacional = sum_edad_nacional / equipo_n if equipo_n else 0
edad_inchas_junior = sum_edad_junior / equipo_j if equipo_j else 0
edad_inchas_bucaramanga = sum_edad_bucaramanga / equipo_b if equipo_b else 0
edad_inchas_medellin = sum_edad_medellin / equipo_med if equipo_med else 0
promedio_dias_estadio = total_dias_estadio / n if n else 0

print(f"el numero de hinchas de Millonarios es: {equipo_m}")
print(f"el numero de hinchas de Nacional es: {equipo_n}")
print(f"el numero de hinchas de Junior es: {equipo_j}")
print(f"el numero de hinchas de Bucaramanga es: {equipo_b}")
print(f"el numero de hinchas de Medellin es: {equipo_med}")
print(f"el promedio de edad de los hinchas de Millonarios es: {edad_inchas_millonarios}")
print(f"el promedio de edad de los hinchas de Nacional es: {edad_inchas_nacional}")
print(f"el promedio de edad de los hinchas de Junior es: {edad_inchas_junior}")
print(f"el promedio de edad de los hinchas de Bucaramanga es: {edad_inchas_bucaramanga}")
print(f"el promedio de edad de los hinchas de Medellin es: {edad_inchas_medellin}")
print(f"articulos preferidos - camiseta: {camisa}, chaqueta: {chaqueta}, gorra: {gorra}, morral: {morral}")
print(f"el promedio de dias al año de los hinchas es: {promedio_dias_estadio}")
