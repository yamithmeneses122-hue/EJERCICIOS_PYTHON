# Eliminacion.
def eliminar_duplicados(arr):
    nuevo = []
    for n in arr:
        if n not in nuevo:
            nuevo.append(n)
    return nuevo
def suma_unicos(arr):
    unicos = eliminar_duplicados(arr)
    suma = 0
    for n in unicos:
        suma += n
    return suma
def promedio_unicos(arr):
    unicos = eliminar_duplicados(arr)
    suma = suma_unicos(arr)
    return suma / len(unicos)
# Interaccion.
entrada = input("\nEjercicio 9 - Ingresa números separados por espacio: ")
arreglo = list(map(int, entrada.split()))
print("Los numeros ingresados fueron:", list)
# Resultados.
suma = suma_unicos(arreglo)
promedio = promedio_unicos(arreglo)
print ("Valores resividos:", entrada)
print("Suma de valores únicos:", suma)
print("Promedio de valores únicos:", promedio)