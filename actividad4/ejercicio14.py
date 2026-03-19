a = [1, 3, 5]
b = [2, 4, 6]

resultado = []
i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        resultado.append(a[i])
        i += 1
    else:
        resultado.append(b[j])
        j += 1

# Agregar lo que sobra
resultado += a[i:]
resultado += b[j:]

print(resultado)