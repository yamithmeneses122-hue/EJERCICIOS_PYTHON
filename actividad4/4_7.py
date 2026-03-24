# Eliminacion.
def eliminar_duplicados(arr):
    nuevo = []
    for n in arr:
        if n not in nuevo:
            nuevo.append(n)
    return nuevo
# Interaccion.
entrada = input("Ejercicio 7 - Ingresa números separados por espacio: ")
arreglo = list(map(int, entrada.split()))

resultado = eliminar_duplicados(arreglo)
print("Sin duplicados:", resultado)