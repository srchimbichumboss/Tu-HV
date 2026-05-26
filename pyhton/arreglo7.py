#Problema 7: En una entidad de salud, se requiere que se atiendan los n
#pacientes que llegan en el transcurso de la noche, de acuerdo al triage
#que reporte el médico asignado a la valoración, para ello se maneja la
#siguiente tabla de clasificación:
#Nivel de urgencia Tipo de urgencia Tiempo de atención
"""1 resucitación Inmediatamente
   2 emergencia 15 min
   3 urgencia 60 min
   4 urgencia menor 2 horas
   5 sin urgencia 4 horas"""
#Para el ingreso a la entidad se debe solicitar los datos personales:
#nombre completo, edad, eps y nivel de urgencia (triage), el programa
#debe mostrar al finalizar:
"""- ¿Cuántos pacientes fueron atendidos
- ¿Si hay un sólo médico de turno, cuánto tiempo le tardará atender
a todos los pacientes
- ¿Cuál es el nivel de urgencia que se presenta con mayor
frecuencia
- El promedio de las edades del triage 3.
- Organizar en un arreglo los nombres de los pacientes de triage 1 e
imprimir el arreglo."""
nombre = 0
edad = 0
eps = 0
nivel_de_urgencia = 0
nivel_triage = [1,2,3,4,5]
c1 = c2 = c3 = c4 = c5 = 0
edad_promedio_triage_3 = 0
nombre_triage_1 = []
#VARIABLES DEF:
def pedir_nombre():
    nombre = (input("\n Escriba el nombre de la persona: "))
    return nombre
def pedir_edad():
    edad = int(input("\n Escriba su edad: "))
    return edad
def pedir_eps():
    eps = (input("\n Escribe su eps: "))
tiempo_total_medico = 0
#damos valor a n:
print("========hospital san pedro claver=========")
n = int(input("ingrese aqui la cantidad de pacientes:"))

for pacientes in range(n):
    print("\n 1: resucitación Inmediatamente")
    print("\n 2: emergencia 15 min")
    print("\n 3: urgencia 60 min")
    print("\n 4: urgencia menor 2 horas")
    print("\n 5: sin urgencia 4 horas")
    nivel_de_urgencia = int(input("\n ingrese aqui el nivel de urgencia: "))

    if nivel_de_urgencia == 1:
        print("¡¡¡RESUCITACION INMEDIATA!!!")
        c1 += 1
        tiempo_total_medico += 0
        nombre_triage_1.append(pedir_nombre())
        pedir_edad()
        pedir_eps()
    elif nivel_de_urgencia == 2:
        print("emergencia en 15 min")
        c2 += 1
        tiempo_total_medico += 15
        pedir_nombre()
        pedir_edad()
        pedir_eps()
    elif nivel_de_urgencia ==3:
        print("emergencia en 60 min")
        c3 += 1
        tiempo_total_medico += 60
        pedir_nombre()
        edad_promedio_triage_3 += pedir_edad()
        pedir_eps()
    elif nivel_de_urgencia ==4:
        print("emergencia en 2 horas")
        c4 += 1
        tiempo_total_medico += 120
        pedir_nombre()
        pedir_edad()
        pedir_eps()
    elif nivel_de_urgencia ==5:
        print("Urgencia en 4 horas")
        c5 += 1
        tiempo_total_medico += 240
        pedir_nombre()
        pedir_edad()
        pedir_eps()
#range con append para evaluarlos """intependiente""":
#clientes_atendidos.append([pacientes])
#contador += 1
    
conteos = [c1,c2,c3,c4,c5]
max_conteo = max(conteos)
nivel_frecuencia = conteos.index(max_conteo) + 1
promedio_triage = (max_conteo/n) * 100
#edad promedio triage 3:
if c3 > 0:
    edad_promedio = edad_promedio_triage_3 / c3
else:
    edad_promedio = 0

#salida,totales: 

"""tiempo atencion un solo medico"""
print("=========================================================================")
print(f" El tiempo que tomara en atender a los pacientes es:",{tiempo_total_medico})
print("---------------------------------------------------------------------------")

print("========================triage mas usado:==================================")
print(f" el triage mas usado es:",{nivel_frecuencia})
print(f" el nivel de urgencia promedio es: ",{promedio_triage},{max_conteo})
print("---------------------------------------------------------------------------")

print("========================promedio edad======================================")
print(f"la edad promedio del triage 3 es: ",{edad_promedio})
print("---------------------------------------------------------------------------")

print("=========================nombres del triage 1===============================")
print("triage 1: ")
#nombres triage 1:
if len(nombre_triage_1)> 1:
    contador1 = 1
    for nom in nombre_triage_1:
        print(f"el nombre de las personas del triage es:",{contador1},{nom})
        contador1 += 1
else:
    print("no hubo personas en el triage 1")
print("--------------------------------------------------------------------------")
