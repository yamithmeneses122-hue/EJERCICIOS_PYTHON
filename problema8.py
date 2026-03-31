# Programa para verificar si una frase es palíndroma

def verificar_palindromo():
    print("--- Verificador de Palíndromos ---")
    
    # 1. Pedir la frase al usuario
    frase_original = input("Ingresa una frase: ")
    
    # 2. Limpiar la frase (basado en métodos de str de la pág. 12)
    # Quitamos espacios y pasamos a minúsculas
    frase_limpia = frase_original.replace(" ", "").lower()
    
    # 3. Invertir la frase usando slicing (técnica de índices de la guía)
    frase_invertida = frase_limpia[::-1]
    
    # 4. Comparar y mostrar el letrero (Sintaxis básica - pág. 4)
    if frase_limpia == frase_invertida:
        print(f"\n¡Éxito! La frase '{frase_original}' ES un palíndromo.")
    else:
        print(f"\nLo siento, la frase '{frase_original}' NO es un palíndromo.")

# Ejecución
verificar_palindromo()