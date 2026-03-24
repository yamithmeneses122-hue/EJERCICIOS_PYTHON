# Ingresar Numeros.
entrada = input("Ingresa números, separados por espacios:")
# lista.
numeros = list(map(int, entrada.split()))
#Si es repetitivo o no.
hay_repetidos = False
# Busca en la lista.
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] == numeros[j]:
            hay_repetidos = True
# Resultados.
if hay_repetidos:
    print("Sí hay elementos repetidos")
else:
    print("No hay elementos repetidos")
