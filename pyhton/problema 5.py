#Problema 4: Le han pedido elaborar un programa para calcular el
#promedio y suma total de salarios que paga un empresario
#mensualmente en su microempresa, con el fin de calcular un incremento
#anual.
#Entrada por trabajador (10): salario, antiguedad_años, y edad para
#poder calcular “promedio de edades”.
#Clasificación por grupos:
"""- A: 0–2 años.
   - B: >2–8 años.
   - C: >8 años."""
#Incremento según promedio salarial del grupo:
"""- A: promedio > 2,000,000 → 4%; si no, 7%.
   - B: promedio > 2,400,000 → 5%; si no, 8%.
   - C: promedio > 3,000,000 → 6%; si no, 10%."""
#Salidas por grupo:
"""- Promedio de salarios.
   - Suma total de salarios.
   - Porcentaje de incremento a aplicar al grupo (no individual).
   - Promedio de edades (si recogemos edad)."""
#generamos variables:
n = 10
salario_trabajador = 0
antiguedad_trabajador = 0
edad_trabajador = 0
#creamos el bucle for i range(2):
for i in range (n):
    print("ingrese su salario:como un entero positivo.")#impresion condicion de el programa.
    salario = int(input("\n ingrese su salario "))
    edad = int(input("\n ingresse su edad: "))
    antiguedad = int(input("\n ingrese su antiguedad en años: "))
    if antiguedad <= 2:#condicionales sobre el salario.
        incremento = 0.04 if salario > 2000000 else 0.07
    elif antiguedad <= 8:
        incremento = 0.05 if salario > 2400000 else 0.08
    else:
        incremento = 0.06 if salario > 3000000 else 0.10
#variables que guarden los datos de los input.
    salario_trabajador += salario
    antiguedad_trabajador += antiguedad
    edad_trabajador += edad

#variables de promedio,suma, y porcentajes.
promedio_salarios = salario_trabajador / n
suma_salarios = salario_trabajador
porcentaje_incremento = incremento + incremento + incremento
promedio_edad = edad_trabajador / n
#salida:
print(f"\n el salario promedio es: {promedio_salarios}")
print(f"\n la suma de los salarios es: {suma_salarios}")
print(f"\n el porcentaje de incremento es: {porcentaje_incremento}")
print(f"\n el promedio de edad es: {promedio_edad}")
