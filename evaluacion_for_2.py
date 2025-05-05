#para sacar nota en el inti es, ejemplo, 50 * 0.3= nota, osea nota por porcentaje da...
#despues asi con las demas hasta despues con esas sacar la nota final
#y para sacar la final solo se suman los resultados y listo

#input guarda en string y si quiero cambiarlo puedo con float o int

nota1 = int(input("coloque su primera nota: "))
nota2 = int(input("coloque su segunda nota: "))
nota3 = int(input("coloque su tercera nota: "))

ponderacion1 = 0.3
ponderacion2 = 0.4
ponderacion3 = 0.3

resultado_ponderacion1 = (nota1 * ponderacion1)
resultado_ponderacion2 = (nota2 * ponderacion2)
resultado_ponderacion3 = (nota3 * ponderacion3)

print(f"su primera ponderacion es {resultado_ponderacion1}")
print(f"su segunda ponderacion es {resultado_ponderacion2}")
print(f"su tercera ponderacion es {resultado_ponderacion3}")

resultado_final = (resultado_ponderacion1 + resultado_ponderacion2 + resultado_ponderacion3)
print(f"su promedio es {resultado_final}")

