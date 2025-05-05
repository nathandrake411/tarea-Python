DESCUENTO_ESTUDIANTE = 0.15
DESCUENTO_CLIENTE_FRECUENTE = 0.10

precio = float(input("Se solicita el precio original de su artículo: "))
usuario = input("¿Qué usuario eres, estudiante o cliente frecuente?: ").lower()

precio_con_descuento = precio

if usuario == "estudiante":
    precio_con_descuento -= precio * DESCUENTO_ESTUDIANTE
    print(f"Descuento estudiante aplicado: {precio * DESCUENTO_ESTUDIANTE}")

elif usuario == "cliente frecuente":
    precio_con_descuento -= precio * DESCUENTO_CLIENTE_FRECUENTE
    print(f"Descuento cliente frecuente aplicado: {precio * DESCUENTO_CLIENTE_FRECUENTE}")

print(f"\nPrecio original: {precio}")
print(f"Precio final con descuento: {precio_con_descuento}")
