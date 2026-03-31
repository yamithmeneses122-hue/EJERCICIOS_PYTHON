# Programa para generar la tabla de multiplicar de un número

def generar_tabla():
    print("--- Generador de Tablas de Multiplicar ---")
    
    # Solicitamos el número al usuario (Sintaxis básica - pág. 4)
    # Convertimos a entero para poder realizar operaciones matemáticas
    numero = int(input("¿De qué número deseas ver la tabla?: "))
    
    print(f"\nTabla de multiplicar del {numero}:")
    
    # Usamos range(1, 11) para multiplicar del 1 al 10 (Funciones - pág. 10)
    for i in range(1, 11):
        resultado = numero * i
        # Mostramos la operación de forma elegante usando f-strings
        print(f"{numero} x {i} = {resultado}")

# Ejecución de la función
generar_tabla()