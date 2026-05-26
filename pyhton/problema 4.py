
"""Problema 5: Una panadería vende los siguientes productos:"""
#Panes:
"""- Integral: $2.000
- Francés: $3.000
- Queso: $1.000"""
"""Pasteles:"""
#- Chocolate: $6.000
#- Manzana: $5.000
"""El programa debe:
- Mostrar los productos y precios.
- Permitir al cliente seleccionar cantidad por producto.
- Calcular el total a pagar.
- Si el total supera $10.000, aplicar descuento del 20%.
- Mostrar el total final después del descuento (si aplica)."""
#se muestran los productos:
print("\n PASTELERIA LAS DELICIAS")
print("\nProductos hoy:")
print("Integral: $2.000")
print("Fraces: $3.000")
print("Queso: $1.000")
print("\n Pasteles")
print("Chocolate: $6.000")
print("Manzana: $5.000")
#seleccion de productos:
producto_seleccionado = input("Integral: A,Frances: B, Queso: C o Chocolate: C, Manzana: E.\n : ")
if producto_seleccionado == "A":
    valor_final = 2000
    try:cantidad = float(input("marque su cantidad: "))
    except:print("error el valor debe ser mayor a 0")

elif producto_seleccionado == "B":
    valor_final = float(3000)
    try:cantidad = float(input("marque su cantidad: "))
    except:print("error el valor debe ser mayor a 0") 

elif producto_seleccionado == "C":
    valor_final = float(1000)
    try:cantidad = float(input("marque su cantidad: "))
    except:print("error el valor debe ser mayor a 0") 

elif producto_seleccionado == "D":
    valor_final = float(6000)
    try:cantidad = float(input("marque su cantidad: "))
    except:print("error el valor debe ser mayor a 0") 

elif producto_seleccionado == "E":
    valor_final = float(5000)
    try:cantidad = float(input("marque su cantidad: "))
    except:print("error el valor debe ser mayor a 0") 
#TOTALES:
total = valor_final * cantidad
#salida:
if total >= 10000:
    try:print(f"\n ¡Obtuviste un descuento del 20%! y el valor final del producto es:  ",(producto_seleccionado),total * 80/100)
    except:print(f"el valor final del producto es:",(producto_seleccionado),total)
#
# 
# 
# 
# 
# print(f"el valor final del producto es:",(producto_seleccionado),total)

#cantidad = input("ingrese su cantidad:")

#1 = 2.000
#2 = 3.000
#3 = 1.000
#4 = 6.000
#5 = 5.000