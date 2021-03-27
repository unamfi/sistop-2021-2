#include <sys/types.h>
#include <stdio.h>
pid_t fork(void);
pid_t getpid(void);
int main(int argc, char *argv[]){
	pid_t pid;

	pid = fork();
	if(pid==-1){
		printf("Fallo en fork\n");
		return -1;
	}else
	if (!pid){
		printf("Proceso hijo: PID %d\n", getpid());
	}else{
		printf("Proceso padre: PID %d\n", getpid());
	}
	return 0;
}
//ejemplo tomado de Procesos e Hilos en C, recuperado de https://www.um.es/earlyadopters/actividades/a3/PCD_Activity3_Session1.pdf
