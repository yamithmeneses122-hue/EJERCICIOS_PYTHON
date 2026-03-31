import math

x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el número de términos de la serie: "))

suma = 1

for i in range(1, n + 1):
    termino = (x ** i) / math.factorial(i)
    suma += termino

print("El valor aproximado de e^x es:", suma)
