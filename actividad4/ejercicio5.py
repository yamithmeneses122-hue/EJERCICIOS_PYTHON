# lista de numeros.
entrada = input("Ingresa números, separados por espacios: ")
numeros = list(map(int, entrada.split()))
# lo que se busca.
buscar = int(input("Ingresa el número que deseas buscar: "))
# si se encontro.
encontrado = False
# Busqueda.
for i in range(len(numeros)):
    if numeros[i] == buscar:
        print("Elemento encontrado en la posición:", i)
        encontrado = True
# Por si no se encuentra.
if not encontrado:
    print("El elemento no está en la lista")
