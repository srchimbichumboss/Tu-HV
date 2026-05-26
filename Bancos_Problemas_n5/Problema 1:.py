"""-------------------Problema 1:------------------------------ 
Una matriz almacena datos de sesiones de clientes con el 
formato: [ID Cliente, Duración (segundos), Eventos Clics]."""
#Se necesita una herramienta para evaluar el nivel de compromiso de 
#cada sesión. 
#Requisitos de Desarrollo: 
""" 
-  Datos Iniciales: 
- Una matriz con al menos 5 filas de datos. 
-  Módulos:  Se  requiere  un  módulo  (función)  para  calcular  la 
clasificación  de  compromiso  de  una  sesión  basándose  en  su 
duración y clics. 
-  Lógica de Negocio: 
✓  Clasificar como "Alto" (si Duración > 180s y Clics > 8). 
✓  Clasificar como "Bajo" (si Duración < 60s o Clics < 3). 
✓  Clasificar como "Medio" en todos los demás casos. 
-  Salida:  
Generar  un  informe  listando  el  ID  del  cliente  y  su 
clasificación final. """

# Matriz vacía para el bucle:
sesiones = []#se puede definir pero vacia genera aletoriedad.

# Solicita al usuario cuántos clientes desea evaluar:
def obtener_numero_clientes():#definimos la funcion y preguntamos cant|clientes.
    while True:
        try:#condicionamos los controles de errores asi el programa no rompe y deja continuar.
            cantidad = int(input("¿Cuántos clientes desea evaluar? "))
            if cantidad >= 5:
                return cantidad#valor para variables especificas.
            print("n\ ¡¡¡La cantidad mínima es 5 clientes. Intente de nuevo!!!")
        except ValueError:#especificamos el errore para evitarlo.
            print("n\ !!!Entrada inválida. Ingrese un número entero.¡¡¡")

# Llena una matriz de sesiones con IDs y datos de duración y|o clics:
def llenar_sesiones(sesiones, cantidad):#definimos la matriz con:sesiones y cantidad pa.
    for indice in range(cantidad):
        id_cliente = 101 + indice#generamos un id cliente especifico y unico para cada cliente.
        duracion = 30 + (indice % 10) * 25#damos un rango min y max.
        clics = 1 + (indice % 12)#aunque el programa real no existe se puede generar aleatoriedad para dar realismoxd.
        sesiones.append([id_cliente, duracion, clics])#evitamos mayusculas y damos formato a la matriz anterior y asi no caemos en la repticion de datos impuestos.

# Módulo para clasificar el compromiso de una sesión
def clasificar_compromiso(duracion, clics):#con el DEF clasificamos el alto bajo y medio (el return nos ayuda con dar resultados especificos de valor)
    if duracion > 180 and clics > 8:#condicionales manejo de duracion y clicks
        return "Alto"
    elif duracion < 60 or clics < 3:#la condicional y el or generan una bicondicional estable 
        return "Bajo"
    else:
        return "Medio"

# Generar informe
def generar_informe(sesiones):#DEF PARA TOTALES FINALES NDJA
    print("ID Cliente | Duración (s) | Clasificación de Compromiso")#IMPRESION CON TABLA
    for sesion in sesiones: #bucle para usar la matrix llenada.
        id_cliente, duracion, clics = sesion
        clasificacion = clasificar_compromiso(duracion, clics)#compilacion, creo.
        print(f"{id_cliente}         | {duracion:>11} | {clasificacion}")

if __name__ == "__main__": #controlamos la ejecucion del programa para que no se rompa.
    numero_clientes = obtener_numero_clientes()
    sesiones = []
    llenar_sesiones(sesiones, numero_clientes)
    generar_informe(sesiones)
    print("-------------Informe final-------------.")
