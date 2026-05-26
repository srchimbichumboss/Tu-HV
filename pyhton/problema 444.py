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
personas = []
for i in range(50):
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
#guardamos un diccionario
    persona ={
    "nombre":nombre_persona,
    "horas":horas_television,
    "canal":canal_preferencia,
    "dinero":dinero_promedio,
    "edad":variable_edad
    }
    personas.append(persona)

for p in personas:
    print(f"""
    Nombre:{p['nombre']}
    Horas:{p['horas']}
    Canal preferido:{p['canal']}
    Pagaria:{p['dinero']}
    Edad:{p['edad']}
    """) 





