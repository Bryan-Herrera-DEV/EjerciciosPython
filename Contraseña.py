"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable.



"""
usr = "Bryanlolry" #credencial usuario
pss = "012345" #credencial password
while(True):
	usuario = input("Introduzca su nombre de usuario: ") #input para reconocer el usuario
	contraseña = input("introduzca su contraseña: ") #input para reconocer el password
	if(usuario == usr and contraseña == pss): #primer if para verificar ambas credenciales
		print("Logro acceder correctamente")
		continue 
	elif(usuario != usr and contraseña == pss): #condicional para verificar si el usuario es incorrecto pero la contraseña si es correcta
		print("El usuario es incorrecto")
		continue
	elif(usuario == usr and contraseña != pss): #condicional para verificar si la contraseña es incorrecta pero el user es correcto
		print("La contraseña es incorrecta")
		continue
	elif(usuario != usr and contraseña != pss): #condicional para verificar si ninguna credencial es correcta
		print("Ninguna credencial es correcta")
