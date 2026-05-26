"""Problema 5: Un gerente de proyectos necesita una herramienta para 
visualizar rápidamente la asignación de recursos y el estado de 
diferentes tareas en su equipo. 
Las tareas y sus estados se representan 
en una estructura de matriz, y se necesita funcionalidad para manipular 
y analizar estos datos. Desarrollar un programa en Python que utilice 
una matriz para representar la asignación de recursos a tareas."""
"""-----------------SOLUCION---------------"""
# Matriz de datos del proyecto: 
# Columna 0: ID de Tarea 
# Columna 1: Estado ("Completado", "Pendiente", "En Curso") 
# Columna 2: Recurso Asignado 
DATOS_PROYECTO = [ 
    [101, "Completado", "Ana"], 
    [102, "Pendiente", "Luis"], 
    [103, "En Curso", "Ana"], 
    [104, "Pendiente", "Marta"] 
] 
 
INDICE_TAREA = 0
INDICE_ESTADO = 1 
INDICE_RECURSO = 2 
 
 
def contar_tareas_por_estado(matriz, estado_objetivo): 
    """Cuenta cuántas tareas tienen un estado específico.""" 
    contador = 0 
 
    for tarea in matriz: 
        if tarea[INDICE_ESTADO] == estado_objetivo: 
            contador += 1 
 
    return contador 
 
 
def obtener_asignaciones_por_columna(matriz): 
    """Trasponer la matriz para agrupar los valores por columna.""" 
    filas = len(matriz) 
    columnas = len(matriz[0]) 
     
    asignacion_por_columna = [] 
    for j in range(columnas): 
        columna_actual = [matriz[i][j] for i in range(filas)] 
        asignacion_por_columna.append(columna_actual) 
 
    return asignacion_por_columna 
 
 
estado_buscado = "Pendiente" 
conteo_pendientes = contar_tareas_por_estado(DATOS_PROYECTO, estado_buscado) 
asignaciones = obtener_asignaciones_por_columna(DATOS_PROYECTO) 
 
print(f"Número de tareas '{estado_buscado}': {conteo_pendientes}") 
print("Asignación de recursos (por columna):") 
for columna in asignaciones: 
    print(columna) 
 
