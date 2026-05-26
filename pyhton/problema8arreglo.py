"""Problema 8: La familia de Pepito ha celebrado sus cumpleaños desde el
primer año de vida, y en el año 2026 cumplirá 6 años, por lo que
nuevamente organizarán una fiesta con familiares y amigos. 
Los padres del niño son muy cuidadosos con sus finanzas y llevan un control
detallado de sus gastos."""
#El año anterior tuvieron un inconveniente con el presupuesto destinado
#a la compra de helados, ya que no lograron llevar un registro exacto.
#Para evitar que esto vuelva a ocurrir, le han solicitado desarrollar un
#programa que permita gestionar la compra y el control del dinero
#disponible.
"""
Requisitos del programa
1. Entrada inicial:
- Solicitar la cantidad de dinero disponible para realizar la
compra de helados.
2. Proceso de compra:
- El usuario podrá comprar la cantidad de helados que desee,
siempre que el dinero alcance.
- Cada helado se selecciona según la siguiente Información:
Tipo Descripción Valor
1 vaso de Helado $2.500
2 choco cono $2.000
3 paleta Drácula $3.800
4 polet $4.500
5 platillo $1.800
"""
"""- Los valores deben almacenarse en un arreglo unidimensional,
donde la posición 0 corresponde al primer tipo de helado, la
posición 1 al segundo, y así sucesivamente:
Posición 0 1 2 3 4
$2.500 $2.000 $3.800 $4.500 $1.800
"""
"""- Después de cada compra, el programa debe mostrar el dinero
restante para que el usuario tenga control del presupuesto.
3. Condiciones para finalizar el ciclo de compra:
"""
"""- Cuando el dinero restante no alcance para comprar ningún tipo
de helado (el programa debe mostrar un mensaje indicando esta
situación)."""
#- O cuando el usuario decida no continuar comprando.
"""Al terminar el proceso, el programa debe mostrar:
• Cantidad total de helados comprados.
• Cantidad de helados por cada tipo.
• Valor total gastado.
• Valor promedio por helado.
• Dinero sobrante."""
#variables definidas de la cada helado con DEF:
def vaso_de_helado():
    helado_vaso = 0
    valor_vaso = 2500
    cantidad_vaso += 1
def helado_de_choco_cono():
    helado_choco = 1
    valor_choco = 2000
    cantidad_choco += 1 
def paleta_dracula():
    helado_dracula = 2
    valor_dracula = 3800
    cantidad_dracula += 1
def helado_polet():
    helado_polet = 3
    valor_polet = 4500
    cantidad_polet += 1
def platillo_de_helado():
    helado_platillo = 4
    valor_platillo = 1800
    cantidad_platillo += 1
#contadores estaticos(posible falla o arreglo):
helado_vaso = 0
helado_choco = 0
#entrada; input para ver la cantidad de dinero disponicle
dinero_disponible = int(input("\n ingrese aqui la cantidad de dinero disponible: "))
#damos valores a las variables de los costes por tipo de helado:
print("el valor de el helado Vaso de helado: $2.500  ")
print("el valor de el helado Choco cono: $2.000 ")
print("el valor de el helado Paleta dracula: $3.800 ")
print("el valor de el helado Polet: $4.500 ")
print("el valor de el helado Platillo: $1.800")
print("\n elija el tipo de Helado segun su numero siendo:")
print("0: Vaso de helado/ 1: Choco cono / 2:Paleta dracula / 3: Polet / 4:Platillo ")
#damos variables equivalentes donde se guarden los datos y las elecciones:
eleccion_helado = int(input("\n Ingrese la cantidad de helados que desee: "))
for i in range(eleccion_helado):
#variables independientes X helado:
    vaso_de_helado()
    helado_de_choco_cono()
    paleta_dracula()
    helado_polet()
    platillo_de_helado()
#variable condicional referente a control de errores:
    if eleccion_helado >= 5 or eleccion_helado <= 0:
        print("¡El numero digitado es incorrecto, intentelo otra vez!")
#agregar mas helados:
    agregar_helado = int(input("\n Desea agregar otro helado? 1:Si / 2:No :"))
    
    if agregar_helado == 2:
        print("Su pedido esta siendo facturado")

    elif agregar_helado == 1:
        vaso_de_helado()
        helado_de_choco_cono()
        paleta_dracula()
        helado_polet()
        platillo_de_helado()
#control errores:
    else:
        print("¡el numero digitado esta mal,intente otra vez!")
"""-----------------------------SALIDAS---------------------------------------"""
#variable TOTAL GASTADO:
total_gastado = dinero_disponible - [valor_vaso],[valor_choco],[valor_dracula],[valor_polet],[valor_platillo] 
#valor PROMEDIO X HELADO:
promedio_helado = [valor_vaso] + [valor_choco] + [valor_dracula] + [valor_polet] + [valor_platillo] / 5 
#valor RESTANTE:
total_restante1 = dinero_disponible - total_gastado
print(f"La cantidad de helados por tipo de helado es:",[cantidad_vaso],[cantidad_choco],[cantidad_dracula],[cantidad_polet],[cantidad_platillo])
print(f"La cantidad de helados comprados por tipo es: ",[cantidad_vaso,valor_vaso],[cantidad_choco,valor_choco],[cantidad_dracula,valor_dracula],[cantidad_polet,valor_polet],[cantidad_platillo,valor_platillo])
print(f"El valor total gastado es:" , total_gastado)
print(f"el valor promedio por helado es: ", promedio_helado)
print(f"El total restante es: ", total_restante1)
