"""Problema 2: Una pequeña empresa necesita automatizar la gestión y el
seguimiento del desempeño de sus ventas para motivar a su equipo.
Actualmente, los datos de ventas se manejan de forma manual, lo que
dificulta la actualización rápida de los registros y la evaluación oportuna
de los incentivos. Se requiere un sistema que pueda llevar un registro
de las ventas por mes y determinar si un vendedor califica para un bono
basado en un límite de ventas predefinido."""

VENTAS_POR_MES = {"enero": 1500, "febrero": 2200, "marzo": 1800}
LIMITE_BONO = 5000
PORCENTAJE_BONO = 0.10  # 10% de bono si supera el límite


def solicitar_datos():
    """Solicita un nombre y ventas de un mes al usuario."""
    nombre_vendedor = input("Ingrese su nombre: ").strip()
    
    if not nombre_vendedor:
        nombre_vendedor = "Vendedor Desconocido"
    
    try:
        cantidad_nueva = float(input("Ingrese las ventas del mes: $"))
        if cantidad_nueva < 0:
            print("Entrada inválida. Las ventas no pueden ser negativas. Usando 0.")
            cantidad_nueva = 0
    except ValueError:
        print("Entrada inválida. Debe ingresar un número. Usando 0.")
        cantidad_nueva = 0
    
    return nombre_vendedor, cantidad_nueva


def agregar_ventas(datos_actuales, mes, monto):
    """Agrega un nuevo mes de ventas al diccionario y retorna el total."""
    datos_actuales[mes] = monto
    return datos_actuales


def revisar_bono(ventas_totales, limite, porcentaje_bono):
    """Verifica si el vendedor califica para un bono y calcula su monto."""
    if ventas_totales >= limite:
        monto_bono = ventas_totales * porcentaje_bono
        print(f"✓ ¡Felicidades! Has alcanzado el límite de ${limite:,.2f}")
        print(f"✓ Ganaste un bono del {porcentaje_bono*100}%: ${monto_bono:,.2f}")
        return monto_bono
    else:
        falta = limite - ventas_totales
        print(f"✗ Aún te faltan ${falta:,.2f} para alcanzar el bono.")
        return 0


def mostrar_resumen(vendedor, ventas_dict, total_ventas, bono_obtenido):
    """Muestra un resumen de las ventas y bonos del vendedor."""
    print("\n" + "=" * 50)
    print(f" RESUMEN DE VENDEDOR: {vendedor.upper()}")
    print("=" * 50)
    
    print("\nDesglose por mes:")
    for mes, monto in ventas_dict.items():
        print(f"  {mes.capitalize():12} -> ${monto:>10,.2f}")
    
    print("-" * 50)
    print(f"{'Total de Ventas':12} -> ${total_ventas:>10,.2f}")
    print(f"{'Bono Obtenido':12} -> ${bono_obtenido:>10,.2f}")
    print("=" * 50)


def main():
    """Función principal del programa."""
    contador = 1
    num_iteraciones = 2
    
    while contador <= num_iteraciones:
        print("\n" + "=" * 50)
        print(f" ITERACIÓN {contador} - REGISTRO DE VENTAS")
        print("=" * 50)
        
        # Solicitar datos del vendedor
        vendedor, nuevas_ventas = solicitar_datos()
        
        # Determinar el mes a agregar
        meses_disponibles = ["abril", "mayo", "junio", "julio", "agosto", "septiembre"]
        mes_actual = meses_disponibles[contador - 1] if contador - 1 < len(meses_disponibles) else f"mes_{contador}"
        
        # Crear una copia del diccionario de ventas para este vendedor
        ventas_vendedor = VENTAS_POR_MES.copy()
        ventas_vendedor = agregar_ventas(ventas_vendedor, mes_actual, nuevas_ventas)
        
        # Calcular total anual
        total_anual = sum(ventas_vendedor.values())
        
        # Revisar si califica para bono
        bono = revisar_bono(total_anual, LIMITE_BONO, PORCENTAJE_BONO)
        
        # Mostrar resumen
        mostrar_resumen(vendedor, ventas_vendedor, total_anual, bono)
        
        # Incrementar contador
        contador += 1
    
    print("\n¡Proceso completado! Gracias por usar el sistema de gestión de ventas.")


if __name__ == "__main__":
    main()
