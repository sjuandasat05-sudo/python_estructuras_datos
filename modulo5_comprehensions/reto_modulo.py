ventas = [
    ("Celular", 2, 800, "Tecnología"),
    ("Mouse", 10, 30, "Tecnología"),
    ("Silla", 3, 250, "Hogar"),
    ("Cuaderno", 20, 10, "Papelería"),
    ("Monitor", 2, 600, "Tecnología"),
    ("Lámpara", 5, 40, "Hogar")
]

print("=== LIST COMPREHENSION ===")

valor_total = [unidades * precio for producto, unidades, precio, categoria in ventas]

print(valor_total)

productos_destacados = [
    producto
    for producto, unidades, precio, categoria in ventas
    if unidades * precio > 1000
]

print(productos_destacados)

print("\n=== DICT COMPREHENSION ===")

producto_info = {
    producto: {
        "valor": unidades * precio,
        "unidades": unidades
    }
    for producto, unidades, precio, categoria in ventas
}

print(producto_info)

ranking_premium = {
    producto: precio
    for producto, unidades, precio, categoria in ventas
    if precio > 50
}

print(ranking_premium)

print("\n=== SET COMPREHENSION ===")

categorias_unicas = {
    categoria
    for producto, unidades, precio, categoria in ventas
}

print(categorias_unicas)

productos_baratos = {
    producto
    for producto, unidades, precio, categoria in ventas
    if precio <= 50
}

print(productos_baratos)

print("\n=== RESUMEN ===")

resumen_formateado = {
    producto: f"${unidades * precio} - {categoria}"
    for producto, unidades, precio, categoria in ventas
    if unidades * precio > 1000
}

print(resumen_formateado)

gran_total = sum(
    unidades * precio
    for producto, unidades, precio, categoria in ventas
)

print("Gran total:", gran_total)

print("\n=== COMPARACIÓN CON FOR ===")

valor_total_for = []

for producto, unidades, precio, categoria in ventas:
    valor_total_for.append(unidades * precio)

print(valor_total_for)