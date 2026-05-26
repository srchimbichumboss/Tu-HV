#Problema 5: 
"""Una matriz registra las horas trabajadas por un equipo 
durante la semana: [Nombre del Recurso, Lunes, Martes, ..., Viernes]. 
Necesitas calcular el total de horas semanales por persona y señalar si 
alguien excedió las horas estándar. 
"""
#Requisitos de Desarrollo 
""" 
- Matriz: Crear una matriz con 4 recursos y horas trabajadas por día 
(valores numéricos). 
- Módulos: Se requiere un módulo (función) para calcular la suma 
total de horas semanales por recurso y clasificar su jornada. 
""" 
#- Lógica de Negocio: 
"""✓ Calcular la suma de horas para cada recurso. 
✓ Clasificar la jornada como "Sobretiempo" si el total de horas 
es mayor al umbral de 40 horas. 
✓ Clasificar como "Horario Estándar" o inferior si no excede 
el umbral.""" 
#- Salida: Imprimir el nombre de cada recurso, su total de horas 
#semanales y la clasificación de su jornada. 
#matriz semana:
#matriz_quincena = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes",
#                    "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", 
#                    "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", 
#]#asumiendo la idea de que paguen cada 15 dias, se repite la semana dos veces.
#matriz Horas:
#matriz_horas = [
#    ["Recurso1", 8, 8, 8, 8, 8],  # Total: 
#    ["Recurso2", 9, 9, 9, 9, 9], 
#   # ["Recurso3", 7, 7, 7, 7, 7], 
#   # ["Recurso4", 10, 14, 10, 10, 11],
#   # ["Recurso5", 6, 6, 6, 6, 6], 
#   # ["Recurso6", 8, 8, 8, 8, 8], 
#   # ["Recurso7", 9, 5, 9, 9, 9], 
#   # ["Recurso8", 7, 7, 7, 7, 7], 
#   # ["Recurso9", 10, 8, 8, 10, 10],
#   # ["Recurso10", 6, 6, 6, 6, 6], 
#   # ["Recurso11", 8, 6, 8, 8, 8], 
#   # ["Recurso12", 9, 6, 9, 9, 9], 
#   # ["Recurso13", 7, 7, 5, 7, 7], 
#   # ["Recurso14", 10, 10, 10, 10, 10],
#   # ["Recurso15", 6, 6, 6, 6, 4], 
#   # ["Recurso16", 8, 1, 8, 8, 8], 
#   # ["Recurso17", 5, 9, 9, 9, 9], 
#   # ["Recurso18", 7, 7, 7, 5, 7], 
#   # ["Recurso19", 10, 10, 10, 5, 10],
#   # ["Recurso20", 6, 6, 4, 6, 6], 
#   # ["Recurso21", 8, 8, 2, 8, 8], 
#   # ["Recurso22", 9, 9, 9, 9, 4], 
#   # ["Recurso23", 7, 5, 7, 7, 7],
#]#23 empleados,5 dias a la semana (x) promedio de horas.
##modulo funcion para calcular horas y clasificar jornada:
#def calcular_horas_y_clasificar(matriz):
#    umbral_horas = 40
#    for recurso in matriz:
#        nombre = recurso[0]
#        horas_semanales = sum(recurso[1:])  # Suma de horas de lunes a viernes
#        if horas_semanales > umbral_horas:
#            clasificacion = "Sobretiempo"
#        else:
#            clasificacion = "Horario Estándar"
#        print(f"{nombre}: Total Horas = {horas_semanales}, Clasificación = {clasificacion}")
##Llamada al módulo:
#calcular_horas_y_clasificar(matriz_horas)
"""hasta este punto es la funcion solicitada,pero se puede hacer una analisis real."""
#arreglos adicionales:
salario_minimo       = 1_750_000
auxilio_transporte   = 250_000
#salario total:  
salario_total        = salario_minimo + auxilio_transporte
umbral_horas         = 40
valor_extra          = 10_000
salario_quincena     = salario_minimo / 2
auxilio_quincena     = auxilio_transporte / 2
semanas_por_quincena = 2
#matriz semana:
matriz_quincena = ["semana1","Lunes", "Martes", "Miércoles", "Jueves", "Viernes",
                   "semana2","Lunes", "Martes", "Miércoles", "Jueves", "Viernes", 
                   "semana3","Lunes", "Martes", "Miércoles", "Jueves", "Viernes", 
]#asumiendo la idea de que paguen cada 15 dias, se repite la semana dos veces.
#matriz Horas:
matriz_horas = [
  ["Recurso1", 8, 8, 8, 8, 8],  # Total: 
  ["Recurso2", 9, 9, 9, 9, 9], 
  ["Recurso3", 7, 7, 7, 7, 7], 
  ["Recurso4", 10, 14, 10, 10, 11],
  ["Recurso5", 6, 6, 6, 6, 6], 
  ["Recurso6", 8, 8, 8, 8, 8], 
  ["Recurso7", 9, 5, 9, 9, 9], 
  ["Recurso8", 7, 7, 7, 7, 7], 
  ["Recurso9", 10, 8, 8, 10, 10],
  ["Recurso10", 6, 6, 6, 6, 6], 
  ["Recurso11", 8, 6, 8, 8, 8], 
  ["Recurso12", 9, 6, 9, 9, 9], 
  ["Recurso13", 7, 7, 5, 7, 7], 
  ["Recurso14", 10, 10, 10, 10, 10],
  ["Recurso15", 6, 6, 6, 6, 4], 
  ["Recurso16", 8, 1, 8, 8, 8], 
  ["Recurso17", 5, 9, 9, 9, 9], 
  ["Recurso18", 7, 7, 7, 5, 7], 
  ["Recurso19", 10, 10, 10, 5, 10],
  ["Recurso20", 6, 6, 4, 6, 6], 
  ["Recurso21", 8, 8, 2, 8, 8], 
  ["Recurso22", 9, 9, 9, 9, 4], 
  ["Recurso23", 7, 5, 7, 7, 7],
]#23 empleados,5 dias a la semana (x) promedio de horas.
#definimos funcion para calcular horas y clasificar jornada:
def calcular_horas_y_clasificar(matriz):
    print("=" * 65)
    print("_"*65)
    print(f"{'RECURSO':<15} | {'TOTAL HORAS':<12} | {'CLASIFICACIÓN':<18}")
    print("="*65)
    for recurso in matriz:
        nombre          = recurso[0]
        horas_semanales = sum(recurso[1:])  # Suma de horas de lunes a viernes
        clasificacion   = "Sobretiempo" if horas_semanales > umbral_horas else "Horario Estándar"
        print(f"{nombre:<15} | {horas_semanales:<12} | {clasificacion:<18}")
    print("=" * 65 + "\n")
#modulo adicional para calcular salario total:
def analisis_salarial_quincena(matriz): #busca con el def,definir una valorable para calcular la quincena
    print("="*70)
    print("_"*70)
    print(f"\nAnálisis Salarial Quincenal:(semanas:{len(matriz_quincena)})")
    print(f"Salario base quincenal: {salario_quincena:>12,.0f}")
    print(f"Auxilio de transporte quincenal: {auxilio_quincena:>12,.0f}")
    print(f"{'RECURSO':<15} {'H.EXTRA (Q)':>12} {'RECARGO (Q)':>15} {'TOTAL QUINCENAL':>18}")
    print("="*70)
#evaluamos bucle final  
for recurso in matriz_horas:
    nombre          = recurso[0]
    horas_semanales = sum(recurso[1:])
    horas_extra     = max(0, horas_semanales - umbral_horas)
    horas_extra_semanal = max(0, horas_semanales - umbral_horas)
    horas_extra_quincena = horas_extra_semanal * semanas_por_quincena
    recargo_extra   = horas_extra * valor_extra
    total           = salario_quincena + auxilio_quincena + recargo_extra
    recargo_extra        = horas_extra_quincena * valor_extra
    print(f"{nombre:<15} {horas_extra_quincena:>9} h   ${recargo_extra:>12,.0f}   ${total:>15,.0f}")
print("=" * 70)
#Llamada al módulo:
calcular_horas_y_clasificar(matriz_horas)
analisis_salarial_quincena(matriz_horas)