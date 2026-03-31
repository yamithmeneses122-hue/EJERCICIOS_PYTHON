# Función para calcular el total del dinero
def calcular_monedero():
    print("--- Contador de Monedero ---")
    
    # Captura de datos usando input() y conversión a entero con int() [cite: 39]
    # Billetes
    b50 = int(input("Cantidad de billetes de $50: "))
    b20 = int(input("Cantidad de billetes de $20: "))
    b10 = int(input("Cantidad de billetes de $10: "))
    
    # Monedas
    m10 = int(input("Cantidad de monedas de $10: "))
    m5 = int(input("Cantidad de monedas de $5: "))
    m1 = int(input("Cantidad de monedas de $1: "))
    
    # Cálculo del total usando operadores aritméticos de suma (+) y multiplicación (*) 
    total = (b50 * 50) + (b20 * 20) + (b10 * 10) + (m10 * 10) + (m5 * 5) + (m1 * 1)
    
    # Mostrar el resultado final usando print() [cite: 39]
    print(f"\nEl total de dinero en el monedero es: ${total}")

# Ejecución de la función
calcular_monedero()