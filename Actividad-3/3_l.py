frase = input("Ingrese frase: ")
f = frase.replace(" ", "").lower()
if f == f[::-1]:
    print("Es palíndromo")
else:
    print("No es palíndromo")