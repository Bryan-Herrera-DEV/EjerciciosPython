"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
while(True):
	cantidad = int(input("Introduzca la cantidad a invertir: "))
	interes = float(input("Introduzca la cantiad de interes anual: "))
	años = int(input("Ingrese el numero de años: "))
	for i in range(años):
		cantidad *= 1 + interes / 100
		print("El capital tras " + str(i+1) + " años es: " + str(round(cantidad, 2)))
