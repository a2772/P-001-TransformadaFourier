import matplotlib.pyplot as plt
import numpy as np
import math as mt
import cmath as cmth

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
	tam = inInt("Ingresa el tamaño de la señal: ","Ingresa un valor entero")
#llenamos la lista
inList=[]
x=[]
aux=0
for i in range(tam):
	inList.append(inFloat(f"Ingresa el valor {i+1} de la señal: ","Ingresa un número"))
	x.append(aux)
	aux+=1
#Ahora pasamos a la parte de los cálculos
xKList=[]#Lista de la gráfica de la suma del valor real con el imaginario (magnitud). En valor absoluto al ser una magnitud
rList=[]#Lista de valores reales
iList=[]#Lista de valores imaginarios
k=0
while k<tam:
	print(f"\nk={k}\n")
	n=0#Cada que termina con una k, reiniciamos n=0
	#Sumamos cada término en parte real e imaginaria con sus valores absolutos:
	real=0
	imaginaria=0
	while n<tam:
		print(f"\tn={n}\n");
		aux=0#Almacena el valor del cálculo
		#Calculamos para cada n el valor real e imaginario
		aux=(k*n*2*3.14159265)/tam
		real+=mt.cos(aux)*inList[n]
		imaginaria+=mt.sin(aux)*inList[n]
		#Redondeo
		imaginaria=round(imaginaria,5)
		real=round(real,5)
		print(f"\t\t->aux={aux}\n")
		print(f"\t\t->in[{n}]={inList[n]}\n")
		print(f"\t\t->cos({aux})={mt.cos(aux)}\n")
		print(f"\t\t->sin({aux})={mt.sin(aux)}\n")
		print(f"\t\t->Real(acumulada)={real}\n")
		print(f"\t\t->Imaginaria(acumulada)={imaginaria}\n")
		n+=1
	#Pasamos a cada vector los valores
	rList.append(real)
	iList.append(imaginaria)
		#Pasando al vector de la magnitud
	absR=0
	absI=0
	if(rList[k]<0):
		absR-=rList[k]
	else:
		absR+=rList[k]

	if(iList[k]<0):
		absI-=iList[k]
	else:
		absI+=iList[k]
	aux=absR+absI
	xKList.append(aux)
	print(f"\n{k}) Parte real: {real}\nParte imaginaria: {imaginaria}\n\n\n")
	k+=1
n=0
while n<tam:
	print(f"\t\t->Posición F[{n}]: {xKList[n]}\n")
	print(f"\t\t->Posición número {n} del vector X: {x[n]}\n")
	n+=1
#Gráfica de la entrada
plt.plot(x,inList,'ro',label="Señal de entrada F[m]")
plt.legend(loc=9)
plt.title("Señal F[m]")
plt.ylabel("F[m]")
plt.xlabel("m")
plt.show()
#Gráfica 1, del módulo o magnitud
plt.plot(x,xKList,'c^',label="Módulo de F(k)")
plt.legend(loc=9)
plt.title("Magnitud FFT")
plt.ylabel("|F(k)|")
plt.xlabel("k")
plt.show()