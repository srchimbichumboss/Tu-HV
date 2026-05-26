"""Problema 2: En un conjunto residencial, cada vecino debe pagar una
cuota mensual para el mantenimiento."""
#El administrador quiere un programa que revise uno por uno a todos los vecinos para lo cual el
#usuario debe ingresar la cantidad de residentes de la unidad residencial
#y el valor de la cuota mensual.
"""Por cada vecino, el sistema debe pedir si ya pagó su cuota o no.
Si el vecino pagó, se registra como “al día”; si no pagó, el programa lo
registra como “moroso”."""
#Este proceso debe repetirse hasta haber revisado a todos los vecinos.
#Al finalizar, el programa muestra cuántas personas están al día y
#cuántas están atrasadas y cuanto es el valor total adeudado por los
#vecinos morosos.
cantidad = int(input("\n Ingrese aqui la cantidad de residentes: "))
valor = int(input("\n Ingrese aqui la valor de la cuota mensual: "))
contador = 0
#ingresamos while por cantidad de residentes:

#ingresamos while por cantidad de residentes:
while contador < cantidad:
    int(input("ingrese el factor:\n 1:Al dia, 0:Moroso"))
    contador += 1
if cantidad == int(1):
    al_dia += 1 
    print(valor * al_dia)
elif cantidad == int(0):
    morosos_resi += 0 
    print(valor *morosos_resi)
totales_finales = aldia * valor
print(f"totales:",{al_dia} ,"dinero:" ,{totales_finales})



##ingresamos while por cantidad de residentes:
#while cantidad > 1:
#    int(input("ingrese el factor:\n 1:Al dia, 0:Moroso"))
#if cantidad == int(1):
#    print(valor * cantidad)
#elif cantidad == 0:
#    print(valor*cantidad)
#cantidad < valor
#continue
##variable:
#al_dia = 1
##totales
#total = valor * 1
#print("el total recojido de los residentes es: \n ", total)


#for cantidad in range():
#    int(input("1:si,2:no"))