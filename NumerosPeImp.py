"""
Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

while(True):
 num = int(input("Ingrese un numero entero: "))
 for x in range(1, num+1, 2): 
 	print(x, end=", ")
