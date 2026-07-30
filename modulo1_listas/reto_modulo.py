notas = [8.5, 4.9, 2.9, 5.0, 1.9, 8.9, 5.0, 2.5]

# 1. calcular el promedio de todas las calificaciones
promedio = sum(notas) / len(notas)
print(f"Promedio general: {promedio:.2f}")


nota_maxima = max(notas)
nota_minima = min(notas)
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")

aprobados = []
for nota in notas:
    if nota >= 3.0:
        aprobados.append(nota)

print(f"Notas aprobadas: {aprobados}")
print(f"Cantidad de aprobados: {len(aprobados)} de {len(notas)}")

# 4. ordenar las calificaciones de mayor a menor
calificaciones_ordenadas = sorted(notas, reverse=True)
print(f"Calificaciones de mayor a menor: {calificaciones_ordenadas}")