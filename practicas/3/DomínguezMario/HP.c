#include<stdio.h>
#include<stdlib.h>
#include<locale.h>
#include<time.h>
#include <omp.h>

void llenarMatriz(int *a[], int n, int ng);
void histograma(int *h, int *a[], int n, int ng);
void printH(int *h, int n);

double inicio, fin;

int main(){

  int i, n = 10000;
  int ng = 256;
  int *a[n], *h;
  setlocale(LC_ALL, "");
  #pragma omp parallel for
    for(i = 0; i < n; i++)
      a[i] = (int*)malloc(n * sizeof(int));

  h = (int*)malloc(ng * sizeof(int));

  llenarMatriz(a, n, ng);
  histograma(h, a, n, ng);
  printf("\n\t\t\tHistograma: \n");
  printH(h, ng);
  printf("\nTiempo de ejecuci�n: %lf", (fin - inicio));
  free(h);
  free(a[n]);
  return 0;
}

void llenarMatriz(int *a[], int n, int ng){
  int i, j;
  time_t t;
  srand((unsigned)time(&t));
  for(i = 0; i < n; i++){
    for(j = 0; j < n; j++){
      a[i][j] = (int)(rand() % ng);
      //sprintf("%d\t ",a[i][j]);
    }
    //printf("\n");
  }
}

void histograma(int *h, int *a[], int n, int ng){
  int i, j;
  inicio = omp_get_wtime();
  int histop[ng];

  for(i = 0; i < ng; i++)
    h[i] = 0;

  #pragma omp parallel private(histop) num_threads(4)
  {
    for(i = 0; i < ng; i++)
      histop[i] = 0;

    #pragma omp for private(j)
      for(i = 0; i < n; i++)
        for(j = 0; j < n; j++)
          histop[a[i][j]]++;

    #pragma omp critical
    {
      for(i = 0; i < ng; i++)
        h[i] += histop[i];
    }
  }
  fin = omp_get_wtime();
}

void printH(int *h, int n){
  int i;
  for(i = 0; i < n; i++){
    if(i % 10 == 0)
      printf("\n");
    printf("%d\t", h[i]);
  }
}
