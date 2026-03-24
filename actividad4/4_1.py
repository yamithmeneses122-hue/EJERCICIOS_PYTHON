# PEDIR NUMEROS SEPARADOS CON ESPACIO.
entrada = input("Ingresa los números, separados por espacios:")

# CORVERTIR EN LISTA.
numeros = list(map(int, entrada.split()))

# SUMA.
suma = 0

# RECORRER LA LISTA GENERADA ANTERIOR MENTE.
for numero in numeros:
    suma += numero

# RESULTADOS.
print("Lista ingresada:", numeros)
print("La suma total es:", suma)