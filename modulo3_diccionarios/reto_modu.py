texto = "python es genial python es facil de aprender python es muy usado"
palabras = texto.split()  # separa el texto en una lista de palabras

# 1. contar la frecuencia de cada palabra usando un diccionario
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print("Frecuencia de palabras:", frecuencia)

# 2. una forma mas corta de hacer lo mismo, usando get() con valor por defecto
frecuencia2 = {}
for palabra in palabras:
    frecuencia2[palabra] = frecuencia2.get(palabra, 0) + 1

print("Frecuencia (con get):", frecuencia2)

# 3. encontrar la palabra que mas se repite
palabra_mas_comun = max(frecuencia, key=frecuencia.get)
print(f"\nLa palabra más repetida es '{palabra_mas_comun}' con {frecuencia[palabra_mas_comun]} veces")

# 4. mostrar el resultado ordenado de mayor a menor frecuencia
ordenado = sorted(frecuencia.items(), key=lambda item: item[1], reverse=True)
print("\nPalabras ordenadas por frecuencia:")
for palabra, veces in ordenado:
    print(f"{palabra}: {veces}")