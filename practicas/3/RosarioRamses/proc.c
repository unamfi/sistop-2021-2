//programa que crea 100 hilos y mide el tiempo medio que le
//llevo crearlos en milisegundos
//tomado de https://www.um.es/earlyadopters/actividades/a3/PCD_Activity3_Session1.pdf
//pagina 6, ejemplo 6

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>

struct timeval t0, t1;
double media = 0.0;

void *hilo(void *arg)
{
	mingw_gettimeofday(&t1, NULL);
	unsigned int ut1 = t1.tv_sec*1000000+t1.tv_usec;
	unsigned int ut0 = t0.tv_sec*1000000+t0.tv_usec;
	media += (ut1-ut0);
}

int main() {
	int i = 0;
	pthread_t h;
	for(i=0;i<100;i++)
	{
		mingw_gettimeofday(&t0, NULL);
		pthread_create(&h, NULL, hilo, NULL);
		pthread_join(h, NULL);
	}
	printf("%f ms\n", (media/100.0));
}
