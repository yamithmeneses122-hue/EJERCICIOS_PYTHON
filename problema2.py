# 1. Solicitar la cantidad de alumnos (N)
n = int(input("Ingrese la cantidad de alumnos: "))

# 2. Inicializar contadores
aprobados = 0
reprobados = 0
nota_minima = 3.0  # depende el sistema varia la nota minima para aprobar.

# 3. Ciclo para leer cada calificación
for i in range(n):
    # Pedimos la nota del alumno actual (i + 1 para que no empiece en 0)
    nota = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
    
    # 4. Determinar si aprueba o reprueba
    if nota >= nota_minima:
        aprobados += 1
    else:
        reprobados += 1

# 5. Mostrar resultados finales
print("-" * 30)
print(f"Total de alumnos aprobados: {aprobados}")
print(f"Total de alumnos reprobados: {reprobados}")