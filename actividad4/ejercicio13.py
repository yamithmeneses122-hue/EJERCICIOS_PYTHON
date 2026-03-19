lista = [3, -1, 5, -7, 2, -4]

negativos = []
positivos = []

for num in lista:
    if num < 0:
        negativos.append(num)
    else:
        positivos.append(num)

resultado = negativos + positivos

print(resultado)