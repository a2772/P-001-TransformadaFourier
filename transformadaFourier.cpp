#include<iostream>
#include<math.h>

using namespace std;

int main(){
	int tam,i,k,n;
	double real,imaginaria,aux;
	printf("Ingresa el tama%co del vector: ",164);
	do{
		while(!scanf("%d",&tam)){
			printf("Ingresa un tama%co v%clido: ",164,160);
			fflush(stdin);
		}
		if(tam<=0)
			printf("Ingresa un tama%co v%clido: ",164,160);
	}while(tam<=0);
	double in[tam],out[tam][2];//arreglo de la entrada ej: [1  1  1] y el de salida (parte real e imaginaria)
	//Posición 0 de out es real, 1 es imaginaria
	for(i=0;i<tam;i++){
		printf("Ingresa el valor %i del vector: ",i+1);
		while(!scanf("%lf",&in[i])){
			printf("Ingresa un valor num%crico: ",130);
			fflush(stdin);
		}
	}
	///Tenemos el vector, procedemos a hacer los cálculos correspondientes
	k=0;
	while(k<tam){//Mientras k sea menor a N-1
		printf("\nk=%i\n",k);
		n=0;//Cada que termina con una k, reiniciamos n=0
		//Sumamos cada término:
		real=0;
		imaginaria=0;
		while(n<tam){
			printf("\tn=%i\n",n);
			aux=0;//Almacena el valor del cálculo
			//Calculamos para cada n el valor real e imaginario
			aux=(k*n*2*3.14159265)/tam;
			real+=cos(aux)*in[n];
			imaginaria-=sin(aux)*in[n];
			printf("\t\t->aux=%lf\n",aux);
			printf("\t\t->in[%i]=%lf\n",n,in[n]);
			printf("\t\t->cos(%lf)=%lf\n",aux,cos(aux));
			printf("\t\t->sin(%lf)=%lf\n",aux,sin(aux));
			printf("\t\t->Real=%lf\n",real);
			printf("\t\t->Imaginaria=%lf\n",imaginaria);
			n++;
		}
		printf("\n%i) Parte real: %lf\nParte imaginaria: %lf\n\n\n",k,real,imaginaria);
		k++;
	}
}
