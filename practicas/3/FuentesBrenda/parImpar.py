##############################################

##Este programa le pide un número entero al usuario y verifica si es
##un número par o impar y muestra en pantalla el resultado.

##############################################

num = int(input("Por favor introduce un numero entero: "))
r = num%2

if (r == 0):
	print("El numero es par :)")

elif (r != 0):
	print("El numero es impar :)")

else:
	print("Hubo un error, lo siento :(")

