promedio = float(input("pon tu promedio de enseñanza media:"))
quintil = int(input("pon el nivel de tu quintil 1,2,3,4,5:"))

valor_arancel = 1800000
valor_matricula = 90000

if 1 >quintil>5:
    print("error coloca solo un numero dentro de lo especificado")
if promedio > 6 and quintil in [1,2]:
    descuento_arancel = 0.20
elif promedio > 6 and quintil in [3,4]:
    descuento_arancel = 0.15
else:
    if 5 < promedio <= 6 and quintil in [1,2]:
        descuento_arancel = 0.13
    elif 5 < promedio <= 6 and quintil in [3,4]:
        descuento_arancel = 0.10
    else:
        promedio <= 5 and quintil in [5]
        descuento_arancel = 0.0

if quintil in [1,2,3]:
    descuento_matricula = 0.10
    if promedio >= 5.5:
        descuento_matricula = 0.5
    else:
        descuento_matricula = 0.10
else:
    descuento_matricula = 0.5

valor_final_arancel = valor_arancel * (1-descuento_arancel)
valor_final_matricula = valor_matricula * (1-descuento_matricula)

print(valor_final_arancel)
print(valor_final_matricula)