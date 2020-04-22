#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
while(True): #bucle para repetir indefinidamente
	horas = int(input("Ingrese el numero de horas trabajadas: ")) #entrada para obtener los datos de horas 
	pago = int(input("Ingrese el salario por hora trabajada: ")) #entrada para obtener los datos de pago por hora
	salrario = horas * pago #operacion del resultado
	print("El salario que usted debe recibir es de " + str(salrario)) 
