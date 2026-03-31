# Programa para capturar 10 números positivos

def capturar_numeros_positivos():
    # Creamos una lista vacía (Estructuras de datos - pág. 11)
    numeros = []
    
    print("Por favor, ingresa 10 números positivos:")
    
    # Bucle for para repetir el proceso 10 veces
    for i in range(1, 11):
        # Bucle while para validar que el número sea positivo
        # Se repite "mientras" la condición sea verdadera
        valido = False
        while not valido:
            num = float(input(f"{i}. Ingresa un número: "))
            
            if num >= 0:
                numeros.append(num) # Agregamos a la lista
                valido = True       # Rompemos el bucle while
            else:
                print("Error: El número debe ser positivo. Inténtalo de nuevo.")
    
    # Listamos los resultados (Sintaxis básica - pág. 4)
    print("\nLos números ingresados son:")
    for n in numeros:
        print(n)

# Ejecución
capturar_numeros_positivos()