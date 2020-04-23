"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente 
demás de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la 
pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

while(True):
	print(">>>PIZZERIA NAPOLI<<<")
	print("> 1)Pizza vegetariana.")
	print("> 2)Pizza no vegetariana.")
	entrada = int(input("Introduce el numero de el tipo de pizza que deseas: "))
	if(entrada == 1):
		print("Ofrecemos los siguientes ingredientes: ")
		print("1)Pimiento")
		print("2)Tofu")
		entrada2 = int(input("Elija el imngrediente que desea: "))
		if(entrada2 == 1):
			pimiento =  int(input("introduzca el numero de pimientos que desea en su pizza: "))
			queso =  int(input("introduzca la cantidad de queso en gramos que desea en su pizza: "))
			tomates =  int(input("introduzca el numero de tomates que desea en su pizza: "))
			print("el numero de pimientos en su orden es " + str(pimiento) + ", su numero de queso es " + str(queso) + ", y su numero de tomates es " + str(tomates))
			continue
		elif(entrada2 == 2):
			tofu =  int(input("introduzca el numero de tofus que desea en su pizza: "))
			queso =  int(input("introduzca la cantidad de queso en gramos que desea en su pizza: "))
			tomates =  int(input("introduzca el numero de tomates que desea en su pizza: "))
			print("el numero de Tofu en su orden es " + str(tofu) + ", su numero de queso es " + str(queso) + ", y su numero de tomates es " + str(tomates))
			continue
		else:
			print("Caracter invalido.")
			continue
	elif(entrada == 2):
		print("Ofrecemos los siguientes ingredientes: ")
		print("1)Peperoni")
		print("2)Jamon")
		print("3)Salami")
		entrada2 = int(input("Elija el imngrediente que desea: "))
		if(entrada2 == 1):
			Peperoni =  int(input("introduzca el numero de Peperoni que desea en su pizza: "))
			queso =  int(input("introduzca la cantidad de queso en gramos que desea en su pizza: "))
			tomates =  int(input("introduzca el numero de tomates que desea en su pizza: "))
			print("el numero de Peperoni en su orden es " + str(Peperoni) + ", su numero de queso es " + str(queso) + ", y su numero de tomates es " + str(tomates))
			continue
		elif(entrada2 == 2):
			Jamon =  int(input("introduzca el numero de Jamon que desea en su pizza: "))
			queso =  int(input("introduzca la cantidad de queso en gramos que desea en su pizza: "))
			tomates =  int(input("introduzca el numero de tomates que desea en su pizza: "))
			print("el numero de Jamon en su orden es " + str(Jamon) + ", su numero de queso es " + str(queso) + ", y su numero de tomates es " + str(tomates))
			continue
		elif(entrada2 == 3):
			Salmon =  int(input("introduzca el numero de Salmon que desea en su pizza: "))
			queso =  int(input("introduzca la cantidad de queso en gramos que desea en su pizza: "))
			tomates =  int(input("introduzca el numero de tomates que desea en su pizza: "))
			print("el numero de Salmon en su orden es " + str(Salmon) + ", su numero de queso es " + str(queso) + ", y su numero de tomates es " + str(tomates))
			continue
		else:
			print("Caracter invalido.")
			continue
	else:
		print("Caracter invalido.")
	
	
		
