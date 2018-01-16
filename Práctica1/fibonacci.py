# -*- coding: utf8 -*-
print('Lee un número de un archivo, y muestra la n-ésima posición de la serie de Fibonacci.')


def fibonacci(x):
	l = 0
	z = 0
	h = 1
	if x == 0:
		return 0
		print('Es 0')
	elif x == 1:
		return 1
		print('Es 1')
	else:	
		for w in range(3,x+1):
			l = z + h
			z = h
			h = l
		return l
		print('El valor de la posición es: ' + str(l))

#Abrimos la lectura del archivo

archivo = open("contieneEntero.txt","r")
#Leo el archivo
primeraLinea = archivo.read()
primeraLinea = int(primeraLinea)
#Crear archivo de salida
archivo1 = open("salida.txt","w")
#Escribir en el archivo de salida
archivo1.write(str(fibonacci(primeraLinea)))
archivo.close()





