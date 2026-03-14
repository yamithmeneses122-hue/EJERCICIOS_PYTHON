# Lista de preguntas
list_preguntas = [
    "¿Cuál es la capital de Colombia?",
    "¿2+2?",
    "¿5 + 3?",
]

# Lista de opciones para cada pregunta
list_respuestas = [
    ["Bogota", "Cali", "Popayan", "Barranquilla"],
    ["3", "4", "5", "7"],
    ["8", "20", "10", "5"]  # corregí la respuesta correcta de 5+3
]

# Índices de la respuesta correcta
respuesta_correcta = [0, 1, 0]

# Contador de preguntas
numero_de_pregunta = 0

# Función para mostrar la pregunta y sus opciones
def cargar_list_pregunta(numero):
    print("\n" + list_preguntas[numero])
    for i, opcion in enumerate(list_respuestas[numero]):
        print(f"{i}: {opcion}")  # f-string para mostrar índice y opción

# Función para verificar la respuesta
def responder(respuesta, numero):
    if respuesta == respuesta_correcta[numero]:
        print("Correcto")
    else:
        print("Mal")

# Función para pasar a la siguiente 0pregunta
def siguiente(numero):
    return numero + 1

# Bucle principal del quiz
while numero_de_pregunta < len(list_preguntas):
    cargar_list_pregunta(numero_de_pregunta)
    respuesta = int(input("Elige una opción: "))
    responder(respuesta, numero_de_pregunta)
    numero_de_pregunta = siguiente(numero_de_pregunta)

print("\nFin del cuestionario")