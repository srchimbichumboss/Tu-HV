INVENTARIO = [
    {"producto": "Camisa Casual",  "stock": 12, "ventas_prom": 5},
    {"producto": "Pantalón Denim", "stock": 4,  "ventas_prom": 8},
    {"producto": "Chaqueta Lona",  "stock": 8,  "ventas_prom": 3},  # Fix 1: string → int
]

STOCK_MINIMO_SEGURIDAD = 10


def calcular_pedido(stock_actual, stock_minimo):
    """Calcula la cantidad a pedir."""
    if stock_actual < stock_minimo:          # Fix 2: > era incorrecto, debe ser 
        return stock_minimo - stock_actual
    else:
        return 0


def clasificar_prioridad(stock):
    """Asigna la prioridad de pedido."""
    if stock < 5:                            # Fix 3: stock_actuall → stock
        prioridad = "Alta"
    elif stock < 10:                         # Fix 4: simplificado (ya sabemos stock >= 5)
        prioridad = "Media"
    else:                                    # Fix 5: elif stock > 10 + pass → else con valor
        prioridad = "Baja"
    return prioridad


def generar_informe_inventario(data):
    for item in data:                        # Fix 6: DATOS_INVENTARIO → data
        stock_actual = item["stock"]         # Fix 7: 'cantidad' → 'stock'
        nombre = item["producto"]

        try:
            stock_actual = int(stock_actual) # Fix 8: convierte stock si llega como string
            cantidad_a_pedir = calcular_pedido(stock_actual, STOCK_MINIMO_SEGURIDAD)
            prioridad_pedido = clasificar_prioridad(stock_actual)
            print(f"Producto: {nombre} | Prioridad: {prioridad_pedido} | Pedir: {cantidad_a_pedir}")
        except Exception as e:
            print(f"Error procesando {nombre}: {e}")


generar_informe_inventario(INVENTARIO)