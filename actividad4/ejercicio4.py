# Lista.
entrada = input("Ingresa números, separados por espacios: ")
numeros = list(map(int, entrada.split()))
# Operaciones.
suma = 0
for numero in numeros:
    suma += numero
media = suma / len(numeros)
# Resultados.
print("La lista es:", numeros)
print("La suma total es:", suma)
print("La media aritmética es:", media)
