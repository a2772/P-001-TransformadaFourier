import matplotlib.pyplot as plt
import numpy as np
import math as mt

#Funciones de entrada
def inInt(message,messageError):
	correcto=False
	while correcto==False:
		try:
			vInt=int(input(message))
			correcto=True
		except ValueError:
			print(messageError)
	return vInt
def inFloat(message,messageError):
	correcto=False
	while correcto==False:
		try:
			vFloat=float(input(message))
			correcto=True
		except ValueError:
			print(messageError)
	return vFloat
#Ejecución
tam = -1
while tam<1:
	tam = inInt("Ingresa el tamaño del vector: ","Ingresa un valor entero")
#llenamos la lista
inList=[]
for i in range(tam):
	inList.append(inFloat(f"Ingresa el valor {i+1} del vector: ","Ingresa un número"))
#Ahora pasamos a la parte de los cálculos
kList=[]#Lista de k's
k=0
while k<tam:
	print(f"\nk={k}\n")
	n=0#Cada que termina con una k, reiniciamos n=0
	#Sumamos cada término:
	real=0
	imaginaria=0
	while n<tam:
		print(f"\tn={n}\n");
		aux=0#Almacena el valor del cálculo
		#Calculamos para cada n el valor real e imaginario
		aux=(k*n*2*3.14159265)/tam
		real+=mt.cos(aux)*inList[n]
		imaginaria-=mt.sin(aux)*inList[n]
		print(f"\t\t->aux={aux}\n")
		print(f"\t\t->in[{n}]={inList[n]}\n")
		print(f"\t\t->cos({aux})={mt.cos(aux)}\n")
		print(f"\t\t->sin({aux})={mt.sin(aux)}\n")
		print(f"\t\t->Real={real}\n")
		print(f"\t\t->Imaginaria={imaginaria}\n")
		n+=1
	print(f"\n{k}) Parte real: {real}\nParte imaginaria: {imaginaria}\n\n\n")
	kList.append(imaginaria)
	k+=1

plt.plot(kList)
plt.show()