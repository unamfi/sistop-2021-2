#include <stdio.h>
#include <stdlib.h>
int main (){
	int *arreglo, num, cont;
	printf("¿Cuantos elementos tiene el conjunto?\n");
	num=5;
	arreglo = (int *)malloc (num * sizeof(int));
	if (arreglo!=NULL) {
		printf("Vector reservado:\n\t[");
		for (cont=0 ; cont<num ; cont++){
			printf("\t%i",*(arreglo+cont));	
		}
		printf("\t]\n");
		printf("Se libera el espacio reservado.\n");  
		free(arreglo);
	}
	return 0;
}
