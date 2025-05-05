#Crea un programa que ayude a un usuario a decidir si una canción es
#adecuada para su playlist basándose en criterios específicos

#Solicita duración de la canción en minutos (float)

duracion = float(input("Duración (min): "))
genero = input("Género: ")
anio = int(input("Año: "))

if duracion < 5 and (genero == "pop" or genero == "rock") and anio > 2010:
    print("Es adecuada para la playlist.")
else:
    print("No es adecuada.")

