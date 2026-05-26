"""Problema 1: Cinemas "Cine Full" desea sistematizar la venta de
entradas y la gestión de sus asientos en una única sala. La sala tiene 5
filas y 10 asientos por fila (una matriz de 5 X 10).
Se debe implementar el siguiente menú de opciones:
Encabezado – Menú: Cine Full
Opción 1. Venta de Asiento
Opción 2. Recolección/Devolución de Asiento.
Opción 3. Mostrar Estado de la Sala.
Opción 4. Salir.
Mensaje en pantalla para ingresar la selección: ¿Cuál es su opción?
Implementar las siguientes funciones:
• inicializar_sala(): Inicializa la sala como una matriz de 5 X 10
donde:
o 0 representa un asiento disponible.
o 1 representa un asiento vendido.
o 2 representa un asiento reservado (por devolver).
o Debe retornar la matriz de la sala.
• mostrar_sala(sala): Imprime el estado actual de la sala de
forma clara, incluyendo las etiquetas de fila y asiento.
• validar_asiento(sala, fila, asiento): Recibe la matriz sala, la
fila (1 a 5) y el asiento (1 a 10).
o Debe verificar si la fila y el asiento están dentro del rango
válido.
o Si son válidos, retorna 1. Si no, retorna 0.
• vender_asiento(sala, fila, asiento): Recibe la matriz sala, la
fila y el asiento.
o Si el asiento es válido y está disponible (0), lo marca
como vendido (1) y retorna el precio del asiento según la
fila: Fila 1-2: $8,000, Fila 3-4: $6,000, Fila 5: $4,000.
o En cualquier otro caso (inválido o ya vendido/reservado),
retorna 0.
• devolver_asiento(sala, fila, asiento): Recibe la matriz sala, la
fila y el asiento.
o Si el asiento es válido y está vendido (1), lo marca como
reservado (2) (para indicar que fue devuelto y está en 
espera de la devolución del dinero) y retorna la penalidad
por devolución: 20% del precio original del asiento.
o Si el asiento es válido y está reservado (2), lo marca
como disponible (0) y retorna -1 (indicando que la
devolución se completó).
o En cualquier otro caso, retorna 0.
Al final del día (al salir del programa), se debe indicar:
1. Ingreso Total Neto por ventas (ventas - devoluciones
completadas).
2. Total de Penalidades acumuladas."""

FILAS = 5
ASIENTOS_POR_FILA = 10


def inicializar_sala():
    """Inicializa la sala como una matriz de 5 x 10 con todos los asientos disponibles."""
    sala = [[0] * ASIENTOS_POR_FILA for _ in range(FILAS)]
    return sala


def mostrar_sala(sala):
    """Imprime el estado actual de la sala de forma clara."""
    print("\n--- Estado de la Sala ---")
    print("     ", end="")
    for asiento in range(1, ASIENTOS_POR_FILA + 1):
        print(f"A{asiento:2d}", end=" ")
    print()
    
    for f in range(FILAS):
        print(f"F{f+1}:  ", end="")
        for estado in sala[f]:
            if estado == 0:
                simbolo = " D "
            elif estado == 1:
                simbolo = " V "
            elif estado == 2:
                simbolo = " R "
            print(simbolo, end=" ")
        print()
    
    print("\nLeyenda: D=Disponible, V=Vendido, R=Reservado (en devolución)")


def validar_asiento(sala, fila, asiento):
    """Verifica si la fila y el asiento están dentro del rango válido."""
    if fila >= 1 and fila <= 5 and asiento >= 1 and asiento <= 10:
        return 1
    else:
        return 0


def obtener_precio(fila):
    """Retorna el precio del asiento según la fila."""
    if fila == 1 or fila == 2:
        return 8000
    elif fila == 3 or fila == 4:
        return 6000
    elif fila == 5:
        return 4000
    return 0


def vender_asiento(sala, fila, asiento):
    """Vende un asiento si está disponible y retorna el precio."""
    if validar_asiento(sala, fila, asiento) == 0:
        return 0
    
    indice_fila = fila - 1
    indice_asiento = asiento - 1
    
    if sala[indice_fila][indice_asiento] == 0:
        sala[indice_fila][indice_asiento] = 1
        return obtener_precio(fila)
    else:
        return 0


def devolver_asiento(sala, fila, asiento):
    """Procesa la devolución de un asiento."""
    if validar_asiento(sala, fila, asiento) == 0:
        return 0
    
    indice_fila = fila - 1
    indice_asiento = asiento - 1
    precio_base = obtener_precio(fila)
    
    if sala[indice_fila][indice_asiento] == 1:
        # Asiento vendido: marcar como reservado y aplicar penalidad
        sala[indice_fila][indice_asiento] = 2
        penalidad = precio_base * 0.20
        return penalidad
    elif sala[indice_fila][indice_asiento] == 2:
        # Asiento reservado: completar devolución
        sala[indice_fila][indice_asiento] = 0
        return -1
    else:
        return 0


def menu_principal():
    """Menú principal del sistema de cine."""
    sala_cine = inicializar_sala()
    ingreso_neto = 0
    total_penalidades = 0
    opcion = 0
    
    while opcion != 4:
        print("\n" + "=" * 40)
        print(" MENÚ: CINE FULL")
        print("=" * 40)
        print("1. Venta de Asiento")
        print("2. Recolección/Devolución de Asiento")
        print("3. Mostrar Estado de la Sala")
        print("4. Salir")
        print("=" * 40)
        
        try:
            opcion = int(input("¿Cuál es su opción? "))
        except ValueError:
            print("Opción no válida. Por favor ingrese un número.")
            continue
        
        if opcion == 1:
            print("\n--- VENTA DE ENTRADAS ---")
            try:
                f = int(input("Ingrese el número de Fila (1-5): "))
                a = int(input("Ingrese el número de Asiento (1-10): "))
            except ValueError:
                print("Fila o Asiento deben ser números.")
                continue
            
            precio_venta = vender_asiento(sala_cine, f, a)
            
            if precio_venta != 0:
                ingreso_neto += precio_venta
                print(f"✓ Venta exitosa. Asiento F{f}-A{a} vendido por ${precio_venta:,}.")
            else:
                print(f"✗ Error en la venta. El asiento no está disponible o es inválido.")
        
        elif opcion == 2:
            print("\n--- RECOLECCIÓN/DEVOLUCIÓN ---")
            try:
                f = int(input("Ingrese el número de Fila (1-5): "))
                a = int(input("Ingrese el número de Asiento (1-10): "))
            except ValueError:
                print("Fila o Asiento deben ser números.")
                continue
            
            resultado = devolver_asiento(sala_cine, f, a)
            
            if resultado > 0:
                total_penalidades += resultado
                print(f"✓ Devolución solicitada para F{f}-A{a}.")
                print(f"  Penalidad aplicada (20%): ${resultado:,.2f}")
            elif resultado == -1:
                precio_base = obtener_precio(f)
                ingreso_neto -= precio_base
                print(f"✓ Devolución completada para F{f}-A{a}.")
                print(f"  Se devolvieron: ${precio_base:,}")
            else:
                print(f"✗ El asiento F{f}-A{a} no se puede procesar.")
        
        elif opcion == 3:
            mostrar_sala(sala_cine)
        
        elif opcion == 4:
            print("\n" + "=" * 40)
            print(" RESUMEN DEL DÍA")
            print("=" * 40)
            print(f"Ingreso Total Neto: ${ingreso_neto:,}")
            print(f"Total de Penalidades: ${total_penalidades:,.2f}")
            print("=" * 40)
            print("¡Gracias por usar el sistema Cine Full!")
        
        else:
            print("Opción no reconocida. Por favor seleccione una opción válida.")


if __name__ == "__main__":
    menu_principal()
