boletin_ofertas = [
    "carlos@correo.com", "juan@correo.com", "mike@correo.com",
    "florence@correo.com", "daisy@correo.com"
]

boletin_noticias = [
    "castañeda@correo.com", "martina@correo.com", "camilito@correo.com",
    "pedrosqui@correo.com"
]

# 1. convertir las listas en conjuntos, esto ya elimina los duplicados internos
suscriptores_ofertas = set(boletin_ofertas)
suscriptores_noticias = set(boletin_noticias)

print("Suscriptores únicos a ofertas:", suscriptores_ofertas)
print("Suscriptores únicos a noticias:", suscriptores_noticias)

# 2. encontrar quienes estan suscritos a AMBOS boletines
suscritos_a_ambos = suscriptores_ofertas & suscriptores_noticias
print(f"\nSuscritos a ambos boletines: {suscritos_a_ambos}")

# 3. encontrar el total de suscriptores unicos (sin importar a cual boletin pertenecen)
todos_los_suscriptores = suscriptores_ofertas | suscriptores_noticias
print(f"Total de suscriptores únicos: {len(todos_los_suscriptores)}")

# 4. encontrar quienes solo reciben ofertas (y no noticias)
solo_ofertas = suscriptores_ofertas - suscriptores_noticias
print(f"Solo reciben ofertas: {solo_ofertas}")