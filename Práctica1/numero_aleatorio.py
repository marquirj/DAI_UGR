# -*- coding: utf8 -*-

import random 

x = random.randrange(1,100)

def numero_aleatorio():
	contador = 0
	correcto = 0
	while contador <=9:
		print ("Introduce un numero:") 
				
		num = input()
		
		contador+=1 
		if x < num:
			print('El número es menor')
		elif x > num:
			 print ('El número es mayor')
		else:
			correcto = 1
			break
	if correcto == 1:
		print ('Acertaste')
	else:
		print('El numero era ' + str(x))
numero_aleatorio()

