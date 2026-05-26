"""Problema 4: 
Diseñe un programa para calcular el valor final de un
producto según su categoría.
Requisitos:"""
#- Definir una constante IVA = 0.19.
#- Solicitar el precio base del producto.
#✓ Si el precio ≤ 0, mostrar error y finalizar.
#- Solicitar el código de categoría:
#✓ Producto básico: no paga IVA.
#✓ Producto estándar: paga IVA del 19%.
#✓ Producto de lujo: paga IVA del 19% + recargo del 5%.
#- Si el código es inválido, mostrar error y finalizar.
#- Calcular y mostrar el valor final según la categoría.
#Definimos la constante del iva
iva = 0.19
#categorias:
Total_producto_basico = "no paga iva"   
Total_producto_estandar = iva
Total_produto_lujo = iva + 0.05
#elejimos
precio_del_producto = int(input("Ingrese el precio del producto:" ))
if precio_del_producto <= 0:
    print("!Error, el valor debe ser mayor a 0¡")
    exit
#Solicitar codigo de categoria    
print("Categoria basica:A")
print("Categoria estandar:B")
print("Categoria de lujo:C")
categoria_producto = int(input(f"\n porfavor introduzca la categoria de su producto:"))
if categoria_producto == "A":
    print("el precio de su producto es:", Total_producto_basico)
elif categoria_producto == "B":
    print("el precio de su producto es:", Total_producto_estandar)
elif categoria_producto == "C":
    print("el precio de su producto es:", Total_produto_lujo)
else:
    print("Error: categoría inválida")

#salida
print(f"su valor total es:", precio_del_producto + categoria_producto)


350


# producto_basico},{producto_estandar},{produto_lujo}"))
