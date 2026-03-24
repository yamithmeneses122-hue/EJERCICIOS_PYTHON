def separar_par_impar(arr):
    pares = []
    impares = []
    
    for n in arr:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    
    return pares, impares

# INTERACCIÓN
entrada = input("\nEjercicio 11 - Ingresa números separados por espacio: ")
arreglo = list(map(int, entrada.split()))

pares, impares = separar_par_impar(arreglo)

print("Pares:", pares)
print("Impares:", impares)