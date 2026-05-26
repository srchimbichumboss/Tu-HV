#Problema 3: Un nuevo operador de televisión por cable desea ofrecer
#nuevos servicios en su ciudad. Para esto, se requiere saber en una
#muestra de 50 personas:
"""- Cuántas horas a la semana invierten en ver televisión.
- Qué tipo de canal prefieren ver: deportivo, cultural, de noticias o
de películas.
- Cuántas personas están dispuestas a pagar más de 50 mil pesos
por el servicio de televisión.
- La edad de la persona"""
#El programa debe mostrar:
"""- El promedio de horas semanales que invierten los encuestados en
ver televisión.
- La cantidad de personas interesadas en cada canal: deportivo,
cultural, de noticias o de películas.
- La cantidad de personas que están dispuestas a pagar más de 50
mil pesos por el servicio.
3
- El promedio de edades de los encuestados."""
#introducimos el bucle:
contador = 0
while contador < 2:
#Asignamos nombre:   
    print("\n Ingrese su nombre: ")
    nombre_persona = input()
#introducciomos las horas a la semana que invierten en ver television:
    print("cuantas horas ve usted television a la semana:")
    horas_television = int(input("ingrese aqui en horas en television: ")) 
#variable de preferencia:
    print("\n deportivo:1, cultura:2, de noticias:3, Peliculas:4")
    canal_preferencia = int(input("ingrese aqui su preferencia de contenido con un numero: "))
#variable de dinero:
    print("\n Estaria usted dispuesto a pagar mas de 50mil pesos por el servicio de television?")
    dinero_promedio = input("\n Marque si o no : ")
#variable de edad:
    variable_edad = int(input("\n ingrese su edad con un numero entero: "))
    contador += 1
#salida
total = nombre_persona , horas_television , canal_preferencia , dinero_promedio , variable_edad

for total in total:
    print(f"\n el nombre de la persona: {nombre_persona} , \n Sus horas en television son:{horas_television} , \n Su canal de preferencia es:{canal_preferencia} , \n Pagaria:{dinero_promedio} , \n Edad:{variable_edad} ")
  
   