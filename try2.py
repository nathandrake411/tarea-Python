promedio_final = float(input("ingrese su promedio de enseñanza media:"))
quintil_socioeconomico = int(input("ingrese si pertenece al quintil socioeconomico 1,2,3,4 o 5:"))

valor_arancel = 1800000
valor_matricula = 90000

if quintil_socioeconomico < 1 or quintil_socioeconomico > 5:
    print("error en los datos ingresados, ingrese numeros dentro de los valores señalados.")
else:
    if promedio_final > 6.0:
        if quintil_socioeconomico in [1,2]:
            descuento_arancel = 0.20
        elif quintil_socioeconomico in [3,4]:
            descuento_arancel = 0.15
        else:
            descuento_arancel = 0.0
    elif 0.5 < promedio_final <= 6.0:
        if quintil_socioeconomico in [1,2]:
            descuento_arancel = 0.13
    elif quintil_socioeconomico in [3,4]:
        descuento_arancel = 0.10
    else:
        0.5 > promedio_final or quintil_socioeconomico == 5
        descuento_arancel = 0.0
    
if quintil_socioeconomico in [1,2,3]:
    if promedio_final >= 5.5:
        descuento_matricula = 0.15
    else:
        descuento_matricula = 0.10
else:
    descuento_matricula = 0.5

valor_final_arancel = valor_arancel * (1-descuento_arancel)
valor_final_matricula = valor_matricula * (1-descuento_matricula)

print(valor_final_arancel)
print("el valor de la matricula es $",valor_final_matricula)



