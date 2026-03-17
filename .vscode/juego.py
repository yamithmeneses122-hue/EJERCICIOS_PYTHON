list_preguntas = [
    "¿cual es la capital de colombia?",
    "¿2+2?",
    "¿5 + 3?",
] 

list_respuestas =[
    ["Bogota","Cali","Popayan","barranquilla"],
    ["3", "4","5","7"],
    ["15","20","10","5"]

]

respuesta_corrcta = [0,1,0],
numero_de_pregunta = 0,
#def es dar ua función 
def cargar_list_pregunta():
   print("\n" +list_preguntas[numero_de_pregunta])

   #in es dentro de una lista por ejemplo, e i es u contado
for i, opcion in enumerate(opciones[numero_de_pregunta])
        print(f"{i}: {list_respuestas}")  #eso es un f string
def respoder(list_respuestas):
    if list_respuestas == respuesta_corrcta[numero_de_pregunta]:
       print("correcto")
    else:
        print("mal")
        
def siguiente():
    retur = numero_de_pregunta
    numero_pregunta += 1
while numero_de_pregunta<(list_preguntas):
    cargar_list_pregunta 
    respuesta = int(input("Elige una opción: "))
    responder=(respuesta)
    siguiente()

print("\nFin del cuestionario")