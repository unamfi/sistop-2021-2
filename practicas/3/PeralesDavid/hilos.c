/*
  NOMBRE: DAVID PERALES RODRÍGUEZ
  FECHA: 24 DE MARZO DEL 2021
  DESCRIPCIÓN: PROGRAMA QUE CREA PROCESOS EN MÁQUINAS GNU/LINUX
*/

# include <sys/types.h>
# include <unistd.h>
# include <stdio.h>
int main ( int argc , char * argv []) {
  pid_t pid ;
  pid = fork () ;
  if ( pid == -1) {
    printf (" Fallo en fork \n ");
    return -1;
  }
  else
    if (! pid ) {
      printf (" Proceso hijo : PID %d\n" , getpid () );
    }
    else {
      printf (" Proceso padre : PID %d \n " , getpid () ) ;
    }
  return 0;
}
