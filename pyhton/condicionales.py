"""
las sentencias son las if,elif,else
"""
#permite ejecutar bloques si se cumplen las condiciones:

import os
os.system("clear")

print("\n sentencia simple condicional")

edad = 18
if edad >= 18:
    print("eres mayor de edad")

print("\n sentencia con el if else")

edad = 16
if edad >= 18:
    print(f"eres mayor de edad")
else:
    print("eres menor de edad")

print("sentencia condicional con la nota de estudiante")
nota = 5
if nota >=9:
    print("sobresaliente")
elif nota >=6:
    print("pasaste")
elif nota >=5:
    print("perdiste")

edad = 17
tiene_carnet = True
if edad >= 18 and tiene_carnet:
    print("excelnte")
else:
    print("pliciaaaaaaaaa")
