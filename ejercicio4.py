print("=== Conversor de Unidades ===")
print("1. Kilómetros a millas")
print("2. Millas a kilómetros")
print("3. Celsius a Fahrenheit")
print("4. Fahrenheit a Celsius")

op = input("Elige una opción (1-4): ")

if op == "1":
    km = float(input("Kilómetros: "))
    if km < 0:
        print("No se permiten distancias negativas.")
    else:
        print(f"{km} km = {km * 0.621371:.2f} millas")

elif op == "2":
    millas = float(input("Millas: "))
    if millas < 0:
        print("No se permiten distancias negativas.")
    else:
        print(f"{millas} millas = {millas / 0.621371:.2f} km")

elif op == "3":
    c = float(input("Celsius: "))
    f = c * 9/5 + 32
    print(f"{c}°C = {f:.2f}°F")
    if c < 0:
        print("Está bajo cero")
    elif 15 <= c <= 25:
        print("Temperatura ambiente")
    else:
        print("Está caliente")

elif op == "4":
    f = float(input("Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c:.2f}°C")
    if c < 0:
        print("Está bajo cero")
    elif 15 <= c <= 25:
        print("Temperatura ambiente")
    else:
        print("Está caliente")

else:
    print("Opción inválida.")
