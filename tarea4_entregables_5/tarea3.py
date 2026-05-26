"""Problema 3: Una pequeña oficina de Recursos Humanos necesita
automatizar el cálculo de los salarios netos de sus empleados a partir de
sus horas trabajadas y una tarifa base, aplicando un descuento fijo. Los
datos iniciales están disponibles, pero el proceso de cálculo, validación y
presentación del informe es propenso a errores manuales. Desarrollar
un programa en Python que maneje una lista de empleados (con sus
horas trabajadas y tarifa por hora), realice el cálculo del salario bruto y
neto (aplicando un descuento del 15%), y genere un informe final."""

# Datos iniciales de los empleados
DATOS_EMPLEADOS = [
    {"nombre": "Ana García", "horas": 160, "tarifa": 15.5},
    {"nombre": "Luis Pérez", "horas": 150, "tarifa": 18.0},
    {"nombre": "Marta López", "horas": 165, "tarifa": 12.0}
]

TASA_DESCUENTO = 0.15


def validar_empleado(empleado):
    """Valida que el empleado tenga datos correctos."""
    try:
        nombre = empleado.get("nombre", "").strip()
        horas = float(empleado.get("horas", 0))
        tarifa = float(empleado.get("tarifa", 0))
        
        if not nombre:
            print("✗ Error: El nombre del empleado no puede estar vacío.")
            return False
        
        if horas < 0:
            print(f"✗ Error: {nombre} tiene horas negativas.")
            return False
        
        if tarifa < 0:
            print(f"✗ Error: {nombre} tiene tarifa negativa.")
            return False
        
        return True
    except (ValueError, TypeError) as e:
        print(f"✗ Error de validación: {e}")
        return False


def calcular_bruto(horas, tarifa):
    """Calcula el salario bruto (horas * tarifa)."""
    return horas * tarifa


def calcular_neto(salario_bruto, tasa_descuento=TASA_DESCUENTO):
    """Calcula el salario neto aplicando el descuento."""
    descuento = salario_bruto * tasa_descuento
    return salario_bruto - descuento


def calcular_descuento(salario_bruto, tasa_descuento=TASA_DESCUENTO):
    """Calcula el monto del descuento."""
    return salario_bruto * tasa_descuento


def generar_informe_individual(empleado):
    """Genera el informe de salario para un empleado."""
    nombre = empleado["nombre"]
    horas = float(empleado["horas"])
    tarifa = float(empleado["tarifa"])
    
    salario_bruto = calcular_bruto(horas, tarifa)
    descuento = calcular_descuento(salario_bruto)
    salario_neto = calcular_neto(salario_bruto)
    
    print("\n" + "=" * 55)
    print(f" INFORME DE SALARIO - {nombre.upper()}")
    print("=" * 55)
    print(f"  Horas Trabajadas:        {horas:>10.1f} hrs")
    print(f"  Tarifa por Hora:         ${tarifa:>9.2f}")
    print("-" * 55)
    print(f"  Salario Bruto:           ${salario_bruto:>9.2f}")
    print(f"  Descuento (15%):         ${descuento:>9.2f}")
    print("-" * 55)
    print(f"  Salario Neto:            ${salario_neto:>9.2f}")
    print("=" * 55)
    
    return {
        "nombre": nombre,
        "bruto": salario_bruto,
        "descuento": descuento,
        "neto": salario_neto
    }


def generar_informe_general(lista_empleados):
    """Genera un informe general de todos los empleados."""
    print("\n" + "=" * 70)
    print(" INFORME GENERAL DE NÓMINA")
    print("=" * 70)
    
    resumen_empleados = []
    total_bruto = 0
    total_descuento = 0
    total_neto = 0
    empleados_procesados = 0
    
    for empleado in lista_empleados:
        if validar_empleado(empleado):
            informe = generar_informe_individual(empleado)
            resumen_empleados.append(informe)
            
            total_bruto += informe["bruto"]
            total_descuento += informe["descuento"]
            total_neto += informe["neto"]
            empleados_procesados += 1
        else:
            print(f"⚠ Empleado skipped: {empleado.get('nombre', 'Desconocido')}")
    
    # Resumen general
    print("\n" + "=" * 70)
    print(" RESUMEN GENERAL")
    print("=" * 70)
    print(f"{'Empleado':<30} {'Bruto':>15} {'Descuento':>15} {'Neto':>15}")
    print("-" * 70)
    
    for emp in resumen_empleados:
        print(f"{emp['nombre']:<30} ${emp['bruto']:>14.2f} ${emp['descuento']:>14.2f} ${emp['neto']:>14.2f}")
    
    print("-" * 70)
    print(f"{'TOTAL':<30} ${total_bruto:>14.2f} ${total_descuento:>14.2f} ${total_neto:>14.2f}")
    print("=" * 70)
    
    print(f"\n✓ Empleados procesados: {empleados_procesados}/{len(lista_empleados)}")
    print(f"✓ Total Nómina Bruta: ${total_bruto:,.2f}")
    print(f"✓ Total Descuentos: ${total_descuento:,.2f}")
    print(f"✓ Total Nómina Neta: ${total_neto:,.2f}")


def main():
    """Función principal del programa."""
    print("\n" + "=" * 70)
    print(" SISTEMA DE GESTIÓN DE NÓMINA - RECURSOS HUMANOS")
    print("=" * 70)
    
    generar_informe_general(DATOS_EMPLEADOS)
    
    print("\n¡Informe de nómina generado correctamente!")


if __name__ == "__main__":
    main()
