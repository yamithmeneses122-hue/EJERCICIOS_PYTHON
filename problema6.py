import random # Importamos el módulo mencionado en la página 16 de tu guía

def generar_par_aleatorio():
    print("--- Generador de Número Par Aleatorio ---")
    
    # Solicitamos el límite al usuario
    limite = int(input("Introduce un número límite: "))
    
    # Verificamos que sea posible encontrar un par menor al límite
    if limite <= 0:
        print("Por favor, introduce un número mayor que 0.")
    else:
        # random.randrange(start, stop, step)
        # Empezamos en 0, terminamos antes del límite, y saltamos de 2 en 2
        numero_par = random.randrange(0, limite, 2)
        
        print(f"El número par aleatorio menor que {limite} es: {numero_par}")

# Ejecutamos el programa
generar_par_aleatorio()