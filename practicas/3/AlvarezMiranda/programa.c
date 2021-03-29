#include <stdio.h>
#include <pthread.h>
#define MAX_THREADS 10
void func(void) {
	printf("ID thread:  %d \n",pthread_self());
	pthread_exit(0);
}
int main() {
	int j;
	pthread_attr_t attr;
	pthread_t th1,th2,th3;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_DETACHED);
	pthread_create(&th1,&attr,func,NULL);
	pthread_create(&th2,&attr,func,NULL);
	pthread_create(&th3,&attr,func,NULL);
	return 0;
}
