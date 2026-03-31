### Ejercicio: Obtener el seno de un ángulo ###

import math # Importamos el módulo math para usar pi y funciones trigonométricas

# 1. Entrada de datos
# Usamos float() porque los grados pueden tener decimales
angulo_grados = float(input("Introduce el ángulo en grados: "))

# 2. Proceso
# Python trabaja el seno en radianes, así que convertimos primero
# Podemos usar la fórmula manual o la función math.radians()
angulo_radianes = math.radians(angulo_grados)

# Calculamos el seno
resultado_seno = math.sin(angulo_radianes)

# 3. Salida de datos
print(f"El seno de {angulo_grados}° es: {resultado_seno}")
