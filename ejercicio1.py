#programa que pida datos para ingresar correctamente

usuario = "pepito"
contraseña = "hola777"

nombre_usuario = input("escribe tu nombre:")
contraseña_usuario = input("escribe tu contraseña:")

if usuario == nombre_usuario and contraseña == contraseña_usuario:
    print("bienvenido pepito")
elif contraseña == contraseña_usuario:
    print("error en validacion de datos")
else:
    print("pista, (h)")

#holaaa