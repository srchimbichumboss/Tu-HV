#PROBLEMAS ESTRUCTURAS REPETITIVAS
"""Problema 1: En un proceso industrial, un horno debe mantener su
temperatura dentro de un rango operativo entre 180 grados Celsius y
200 grados Celsius."""
#El sistema debe monitorear continuamente la
#temperatura y emitir una alerta si se sale del rango.
#El sistema debe monitorear continuamente la temperatura del horno. En
#cada iteración:
"""Solicite una temperatura entera positiva en °C (valide).
Si temperatura > 200 → “Alerta: enfriamiento”.
Si temperatura < 180 → “Alerta: calentamiento”.
En caso contrario → “Temperatura óptima”.
Pregunte 
“¿Desea continuar? (1: sí, 0: no)”. Si el usuario ingresa 0,
termina el monitoreo."""

#Temperatura =int(input("Coloque la temperatura del Horno en  entera positiva en °C:\n"))
#while Temperatura > int(200):
#    print("Alerta: enfriamiento")
#    if Temperatura < 180:
#        print("alerta: de calentamiento")
#        Exception: print("temperatura optima.")

temperatura =int(input("Coloque la temperatura del Horno en  entera positiva en °C:\n"))
if temperatura > 200:
    print("Alerta:Enfriamiento")
elif temperatura < 180:
    print("Alerta:Calentamiento")
else:
    print("Temperatura optima")

continuar = int(input(f"¿Desea continuar? (1:si, 0:no)"))
if continuar == 1:
    temperatura =int(input("Coloque la temperatura del Horno en  entera positiva en °C:\n"))
if temperatura > 200:
    print("Alerta:Enfriamiento")
elif temperatura < 180:
    print("Alerta:Calentamiento")
else:
    print("Temperatura optima")

continuar = int(input(f"¿Desea continuar? (1:si, 0:no)"))
if continuar == 0:
    print("a terminado el proceso")
    exit

175













    
#if Temperatura < 180:
#    print(“Alerta: calentamiento”)


        