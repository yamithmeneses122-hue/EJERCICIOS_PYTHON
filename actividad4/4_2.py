# Numeros.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
# Maximo o Minimo.
if num1 > num2:
    maximo = num1
    minimo = num2
elif num2 > num1:
    maximo = num2
    minimo = num1
else:
    print("Ambos números son iguales:", num1)
    exit()
# Resultado final.
print("El número máximo es:", maximo)
print("El número mínimo es:", minimo)