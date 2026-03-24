def contar(arr, valor):
    contador = 0
    for n in arr:
        if n == valor:
            contador += 1
    return contador
# Interaccion.
entrada = input("\nEjercicio 8 - Ingresa números separados por espacio: ")
arreglo = list(map(int, entrada.split()))
valor = int(input("Ingresa el número a contar: "))
resultado = contar(arreglo, valor)
print("El número aparece", resultado, "veces")
