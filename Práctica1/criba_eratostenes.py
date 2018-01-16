# -*- coding: utf8 -*-
print ('Introduce un número:')
x = int(input())

miLista = range(0,x)

for z in range(2,len(miLista)):
	
	for w in range(2,len(miLista)):
		if (z % w)==0:
			for h in range(w,(len(miLista)+1)):
				l = h * w
				if l in miLista:
					miLista.remove(l)
print( miLista)
