# Programa para calcular el factorial de los números del 1 al 10

def calcular_factoriales():
    print("--- Factoriales del 1 al 10 ---")
    
    # Usamos range(1, 11) para incluir los números del 1 al 10
    for numero in range(1, 11):
        factorial = 1
        
        # Calculamos el factorial del número actual
        for i in range(1, numero + 1):
            factorial *= i  # Operador de asignación (multiplicación)
            
        print(f"El factorial de {numero} es: {factorial}")

# Llamada a la función
calcular_factoriales()
