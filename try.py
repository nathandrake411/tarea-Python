# Valores base
valor_arancel = 1800000
valor_matricula = 90000

# Entrada de datos
promedio = float(input("Ingrese su promedio: "))
quintil = int(input("Ingrese el quintil (1, 2, 3, 4 o 5): "))

# Validación de quintil
if quintil < 1 or quintil > 5:
    print("Error: el quintil debe estar entre 1 y 5.")
else:
    # Calcular descuento en arancel
    if promedio > 6.0:
        if quintil in [1, 2]:
            descuento_arancel = 0.20
        elif quintil in [3, 4]:
            descuento_arancel = 0.15
        else:
            descuento_arancel = 0.0
    elif 5.0 < promedio <= 6.0:
        if quintil in [1, 2]:
            descuento_arancel = 0.13
        elif quintil in [3, 4]:
            descuento_arancel = 0.10
        else:
            descuento_arancel = 0.0
    else:
        descuento_arancel = 0.0

    # Calcular descuento en matrícula
    if quintil in [1, 2, 3]:
        if promedio >= 5.5:
            descuento_matricula = 0.15
        else:
            descuento_matricula = 0.10
    else:
        descuento_matricula = 0.0

    # Cálculo de valores finales
    valor_final_arancel = valor_arancel * (1 - descuento_arancel)
    valor_final_matricula = valor_matricula * (1 - descuento_matricula)

    # Mostrar resultados
    print(f"\nEl valor del arancel es: ${valor_final_arancel:,.0f}")
    print(f"El valor de la matrícula es: ${valor_final_matricula:,.0f}")
