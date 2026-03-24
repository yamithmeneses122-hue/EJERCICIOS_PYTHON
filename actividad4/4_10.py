# 
def concatenar(a, b):
    return a + b
# Interaccion.
entrada1 = input("Ingresa el primer arreglo: ")
entrada2 = input("Ingresa el segundo arreglo: ")
arreglo1 = list(map(int, entrada1.split()))
arreglo2 = list(map(int, entrada2.split()))
# Resultados.
resultado = concatenar(arreglo1, arreglo2)
print("Arreglo concatenado:", resultado)