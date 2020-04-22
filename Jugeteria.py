"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los 
payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea 
el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

payaso = 112
muñeca = 75
while(True):
	print("Jugeteria Bryanlolry")
	print(" 1)Introducir el numero de payasos y muñecas de la compra")
	print(" 2)Salir")
	ent = int(input("Introduce el caracter de la accion a realizar: "))
	if(ent == 1):
		pysC = int(input("Introduzca el numero de payasos en la compra: "))

		mñsC = int(input("Introduzca el numero de muñecas en la compra: "))

		pesoT = (payaso * pysC) + (muñeca * mñsC)

		print("El numero de muñecas es " + str(mñsC) + " y el numero de payasos es " + str(pysC) + " con un peso total de" + str(pesoT))
		continue
	else:
		break	
		
