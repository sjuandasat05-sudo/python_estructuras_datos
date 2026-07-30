inventario = [
    ("celular", 78000, 10),
    ("reloj", 40000, 15),
    ("casa", 50000, 5),
    ("parlantes", 6000, 8),
]

print("Valor por producto:")
valor_total_inventario = 0

for producto in inventario:
    nombre, precio, cantidad = producto
    valor_producto = precio * cantidad
    valor_total_inventario += valor_producto
    print(f"- {nombre}: {cantidad} unidades x {precio} = {valor_producto}")

print(f"\nValor total del inventario: {valor_total_inventario}")


producto_mas_caro = max(inventario, key=lambda producto: producto[1])
print(f"Producto más caro: {producto_mas_caro[0]} ({producto_mas_caro[1]})")


producto_mas_stock = max(inventario, key=lambda producto: producto[2])
print(f"Producto con más stock: {producto_mas_stock[0]} ({producto_mas_stock[2]} unidades)")