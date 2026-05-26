"""Problema 3: Se requiere una herramienta para auditar el inventario y 
decidir qué artículos necesitan ser reabastecidos. La información se 
encuentra en una matriz: [Código Artículo, Nombre, Stock Actual, Stock 
Mínimo Requerido].""" 
 
#-Requisitos de Desarrollo 
""" 
- Matriz: Crear una matriz con al menos 5 artículos. 
- Módulos: Se requiere un módulo (función) para determinar la 
cantidad exacta a pedir para un artículo. 
""" 
#- Lógica de Negocio: 
"""✓ Si el Stock Actual es menor al Stock Mínimo, la cantidad 
a pedir es la diferencia (Mínimo Requerido - Stock Actual). 
✓ Si el Stock Actual es suficiente (mayor o igual al Mínimo), 
la cantidad a pedir es cero. 
- Salida: Imprimir una lista de pedidos que muestre el nombre del 
artículo y la cantidad exacta que debe ser solicitada. """
#Matriz de inventario:
matriz_inventario = [#matriz con almenos 25 artuculos.
    ["A001", "Lápiz", None, 100],#El objetivo es dar una cantidad similar a un stock real.
    ["A002", "Cuaderno", None, 50],
    ["A003", "Borrador", None, 25],
    ["A004", "Regla", None, 20],
    ["A005", "Marcador", None, 15],
    ["A006", "Tijeras", None, 10],
    ["A007", "Pegamento", None, 12],
    ["A008", "Carpeta", None, 30],
    ["A009", "Calculadora", None, 5],
    ["A010", "Esmalte", None, 4],
    ["A011", "Impresion", None, 3],
    ["A012", "Escaneo", None, 2],
    ["A013", "Recarga", None, 6],
    ["A014", "Cartulina", None, 2],
    ["A015", "Fomi", None, 1],
    ["A016", "Sacapuntas", None, 4],
    ["A017", "Pintura", None, 3],
    ["A018", "Plastilina", None, 2],
    ["A019", "Audifonos", None, 5],
    ["A020", "Flauta", None, 4],
    ["A021", "Cera", None, 2],
    ["A022", "Arcilla", None, 5],
    ["A023", "Incopor", None, 3],
    ["A024", "Cinta", None, 2],
    ["A025", "Libreta", None, 6],
    ["A026", "Papel", None, 4],
    ["A027", "Tiza", None, 3],
    ["A028", "Compas", None, 2],
    ["A029", "Silla", None, 10],
    ["A030", "Pistola", None, 5],
    ["A031", "Silicona", None, 3],
]
#ALGO ADICIONAL AL EJERCICIO PARA QUE NO ESTE TAN MUERTO XD:
for articulo in matriz_inventario:#con este bucle corto le damos vida.(llena el None o vacio)
    articulo[2] = input(f"Ingrese el stock actual del artículo en inventario '{articulo[1]}': ").strip()#el strip elimina espacios.
#Damos titulos:
print("="*85)
print("\n 00=========================Reportes de los pedidos===============================00")
print("="*85) #modulos para la recopilacion del stand: 
print(f"| {'Código':<8} | {'Artículo':<18} | {'Stock Act':>13} | {'Stock Mín.':>13} | {'A Pedir':>12} |")  
#solicita la diferencia entre los stocks asi determinamos cuanto falta en el inventario.
for articulo in matriz_inventario:
    Codigo, Nombre_articulo, Stock_actual, Stock_minimo = articulo
    try:#Necesitamos que sea un entero(int):
        Stock_actual = int(Stock_actual)
        Stock_minimo = int(Stock_minimo)
        if Stock_actual <  Stock_minimo :
           Total_a_pedir = Stock_minimo - Stock_actual#el valueerror controla ese error especifico.
        else: 
            cantidad_a_pedir = 0
            print(f"No hay necesidad de pedir mas,El stock minimo cumple:{Nombre_articulo}")    
    except ValueError:
        print("¡¡¡La cantidad digitada es superior a la permintida en el inventario!!!")
        Stock_actual = 0
        cantidad_a_pedir = 0
#Salida final,porfinxd:
    print(f"| {Codigo:<8} | {Nombre_articulo:<18} | {Stock_actual:>13} | {Stock_minimo:>13} | {Total_a_pedir:>12} |")

  
