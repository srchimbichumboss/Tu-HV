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
#Variables:
salario = 2000000
#Entrada:
trabajado = []
for antiguedad_años in range(2):
    antiguedad_años =int(input("\n Cuantos años llevas en la empresa?" ))
    if antiguedad_años <= 2:
        antiguedad_añosA = print(f"su promedio es:",int(salario))
    elif antiguedad_años <= 8:
        antiguedad_añosB = print(f"su promedio es:",int(salario))
    elif antiguedad_añosC >=8:
        antiguedad_añosC = print(f"su promedio es:",int(salario))
#edades del grupo        
edades = []
for edades_grupo in range(2):
    edades_grupo = int(input("\n Que edad tiene: "))
#suma salarios:
antiguedad_añosA = 2000000
antiguedad_añosB = 2400000
antiguedad_añosC = 3000000
suma_salarios = antiguedad_añosA + antiguedad_añosB + antiguedad_añosC
#salida:
print(f"el promedio de salarios es: ", antiguedad_añosA + antiguedad_añosB + antiguedad_añosC / 6)
print(f"la suma total de salarios es: ", suma_salarios )
print(f"porcentaje de incremento a aplicar al grupo: ")
print(f"el promedio de edad es: ", edades_grupo / 2)