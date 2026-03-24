# funcion para la invercion.
def invertir(arreglo):
    invertido = []
    
    for i in range(len(arreglo) - 1, -1, -1):
        invertido.append(arreglo[i])
    return invertido


# Datos que ingresa.
entrada = input("Ingresa una lista de números, separados por espacios:")
# convercion.
arreglo = [int(num) for num in entrada.split()]
# Funcion.
resultado = invertir(arreglo)
# Resultados.
print("Arreglo original:", arreglo)
print("Arreglo invertido:", resultado)