"""Problema  2:  Se  gestionan  los  precios  de  un  menú  de  restaurante.  El 
menú se representa como una matriz: [Nombre del Producto, Categoría, 
Precio Base].  
"""
#Se  requiere  una  funcionalidad  para  aplicar  una  promoción  a  productos 
#específicos. 

#Requisitos de Desarrollo 
""" 
-  Matriz:  Crear  una  matriz  con  al  menos  6  productos  de  diversas 
categorías. 
-  Módulos: Se requiere un módulo (función) para calcular el precio 
final de un producto. 
-  Lógica de Negocio: 
✓  Aplicar un 15% de descuento si el producto cumple con la 
categoría objetivo, específica y su precio base es mayor a 
un umbral definido. 
✓  Mantener el precio base si no se cumplen las condiciones. 
-  Salida: Mostrar cada producto, su precio base y el precio final con 
la promoción aplicada. """
#matriz productos: tendra nombre del producto, categoria y precio base;
matrix = [
    ["Cuchuco", "almuerzo", 8.500],
    ["Sopa de pasta", "Sopa", 7.000],
    ["Bandeja paisa", "Menu especial", 17.000],
    ["Arroz con leche", "Menu especial", 5.500],
    ["Fruta", "Saludable", 6.500],#matriz con 6 productos especificos 
    ["Sancocho trifasico", "Sopa", 9.000],
    ["jugo en leche", "Adicionales jugos", 6.000],
    ["Arroz con pollo", "Almuerzo", 7.000],
    ["Picada", "Comida Rápida", 19.000],
]
#Modulo para calcular el precio final con su respectiva promocion:
def calcular_precio_final(producto, categoria_objetivo, umbral):#definimos una función con los datos anteriores.
    nombre, categoria, precio_base = producto
    if categoria == categoria_objetivo and precio_base > umbral:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base
    return precio_final
# reemplazamos la ENTRADA del cliente estática:
def mostrar_menu(menu):#imprimimos menu.
    print("\n Bienvenido, Menú disponible:")#imprimimos menu.
    for i, item in enumerate(menu, start=1):
        nombre, categoria, precio = item
        print(f"{i}. {nombre} ({categoria}) - ${precio:.2f}")#imprimimos menu.

def solicitar_entero(prompt, min_val=None, max_val=None):#condicionales manejo de errores.
    while True:#los ---None-- no anidados permiten que el usuario ingrese un rango.
        try:
            val = int(input(prompt))#variables por valores totales con rangos definidos
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print("¡¡¡Valor invalidp, Intente de nuevo.!!!")
                continue
            return val
        except ValueError:
            print("¡¡¡Entrada inválida, Porfavor ingrese un número entero.!!!")

def generar_factura(cliente_id, items, empresa=False):#evaluamos el print de laa factura.
    if empresa:
        titulo = "Factura Total - Restaurante Las Delicias de Barbosa"
    else:
        titulo = f"Factura Cliente #{cliente_id} - Restaurante Las Delicias de Barbosa"
    print("\n" + titulo)
    print("Producto | Categoria | Precio unitario | Cantidad | Total")
    subtotal = 0.0 #variable donde guardaremos el valor de la factura.
    for nombre, categoria, precio_unitario, cantidad, precio_final_unit in items:
        total_linea = precio_final_unit * cantidad
        subtotal += total_linea #contadores que incrementen.
        print(f"{nombre} | {categoria} | ${precio_unitario:.2f} | {cantidad} | ${total_linea:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")#preparamos los sub totales(facturas ombe) por cliente.
    print("BON APETITE XD.\n")

def main():
    categoria_objetivo = "Menu especial"
    umbral = 10.00#promocion por ensima del producto basico minimo.
#impresion final.
    print("0================Bienvenido al Restaurante Las Delicias de Barbosa==========0")
    numero_clientes = solicitar_entero("\n ¿Cuántos clientes desean a pedir? (mínimo 1, numero entero): ", min_val=1)
    print("\nSeleccione el tipo de cuenta:")
    print("1. Separada")
    print("2. Compartida")
    tipo_cuenta = solicitar_entero("Ingrese 1 para separada o 2 para compartida: ", min_val=1, max_val=2)
    modo_cuenta = 'separada' if tipo_cuenta == 1 else 'compartida'
    mostrar_menu(matrix)

    totales_empresa = {}

    for cliente in range(1, numero_clientes + 1):#el range se usa de iterable y realiza el conteo y lista los clientes
        print(f"\n--- Cliente {cliente} ---")
        pedidos_cliente = []
        while True:#bucle que transmite informacion sobre el pedido y regula errores.
            opcion = solicitar_entero("Seleccione el número del producto (0 para terminar): ", min_val=0, max_val=len(matrix))
            if opcion == 0:
                break#condicional de roptura del bucle si el cliente digita 0 es = a fin.
            producto = matrix[opcion - 1] # indice obligatorio X producto.
            cantidad = solicitar_entero("Cantidad: ", min_val=1)#ejecutamos para multiplicar la cantidad del producto.
            nombre, categoria, precio_unitario = producto
            precio_final_unit = calcular_precio_final(producto, categoria_objetivo, umbral)
            pedidos_cliente.append((nombre, categoria, precio_unitario, cantidad, precio_final_unit))# nNoS AsEGuramos de que las mayusculas no intervengan y las

            key = nombre #la llave (o key)funciona como id del cliente especifico.
            if key not in totales_empresa:
                totales_empresa[key] = {"categoria": categoria, "precio_unitario": precio_unitario, "cantidad": 0, "total": 0.0}
            totales_empresa[key]["cantidad"] += cantidad
            totales_empresa[key]["total"] += precio_final_unit * cantidad#seguimos asegurando el incremente de variables.

            mas = input("¿Desea añadir otro producto este cliente? responder con :(s/n): ").strip().lower()#control MAyUsCULAS
            if mas != 's':
                break#un continiu era mejor pero el break es directo y evita errores en el bucle.

        if modo_cuenta == 'separada':
            generar_factura(cliente, pedidos_cliente, empresa=False)#el False es por que no es el total de la empresa asi controlamos esa variable.

    #Factura total para la empresa
    items_empresa = []#items es la variable especifica de la empresa.
    for nombre, datos in totales_empresa.items():
        cantidad = datos["cantidad"]
        total = datos["total"]
        precio_unitario = datos["precio_unitario"]
        precio_final_unit_prom = total / cantidad if cantidad else precio_unitario
        items_empresa.append((nombre, datos["categoria"], precio_unitario, cantidad, precio_final_unit_prom))#totales y control mayusculas.

    generar_factura("Totales", items_empresa, empresa=True)

if __name__ == "__main__":#el name_main_ es para asegurar el bucle y la ejecucion especifica del programa y no se repita y muera todo.
    main()
    