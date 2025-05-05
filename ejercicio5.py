biblioteca = ["1984", "Cien años de soledad", "El Principito", "Harry Potter", "Orgullo y prejuicio"]

while True:
    print("\n1. Ver libros")
    print("2. Buscar libro")
    print("3. Agregar libro")
    print("4. Eliminar libro")
    print("5. Salir")
    op = input("Opción (1-5): ")

    if op == "1":
        for libro in biblioteca:
            print("-", libro)

    elif op == "2":
        nombre = input("Nombre del libro: ")
        if nombre in biblioteca:
            print("Sí está en la biblioteca.")
        else:
            print("No se encontró el libro.")

    elif op == "3":
        nuevo = input("Libro a agregar: ")
        if nuevo in biblioteca:
            print("Ya existe.")
        else:
            biblioteca.append(nuevo)
            print("Libro agregado.")
            if len(biblioteca) > 10:
                print("Límite alcanzado: versión gratuita llena.")

    elif op == "4":
        borrar = input("Libro a eliminar: ")
        if borrar in biblioteca:
            biblioteca.remove(borrar)
            print("Libro eliminado.")
        else:
            print("No está en la biblioteca.")

    elif op == "5":
        print("Adiós.")
        break

    else:
        print("Opción no válida.")
