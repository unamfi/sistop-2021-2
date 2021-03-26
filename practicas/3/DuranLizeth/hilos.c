/*
* Durán González Lizeth
* Sistemas Operativos 
* Programa sencillo usando hilos 
*/

#include <stdio.h>
#include <pthread.h>

void *threadCreado (void *info)
{
  char *data = (char*)info;
  printf ("-> \n %s", data);
}


int main(int argc, char const *argv[])
{
  pthread_t thread1;
  pthread_t thread2;
  pthread_t thread3;

  pthread_create(&thread1, NULL, &threadCreado, "Lizeth");
  pthread_create(&thread2, NULL, &threadCreado, "Durán");
  prhread_create(&thread3, NULL, &threadCreado, "González");

  return 0;
}
