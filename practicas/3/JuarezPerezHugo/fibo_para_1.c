//fibo_para_1.c
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <stdint.h>
#include <windows.h>

double  fibo_pd( int n , double a[])
{ 
    long double i,j;

    if ( a[n] == 0 ){
        
        #pragma omp task shared( i ) firstprivate ( n )
        i = fibo_pd(n - 1, a );

        #pragma omp task shared( j ) firstprivate ( n )
        j = fibo_pd(n - 2, a );

        #pragma omp taskwait
        a[n] = i + j;
    }

    return a[n];
}


int main(int argc, char** argv )
{
    unsigned n = atoi(argv[1]);
    
    double a[n];
    
    for (size_t i = 0; i < n; i++)
    {
        a[i] = 0;
    }
    

    a[0] = 1; 
    a[1] = 1;  

    double res;

    LARGE_INTEGER frequency;
    LARGE_INTEGER start;
    LARGE_INTEGER end;
    double interval;

    QueryPerformanceFrequency(&frequency);
    QueryPerformanceCounter(&start);


    #pragma omp parallel default ( none ) shared(res, a, n) num_threads( 4 )
    {
        #pragma omp single 
        res = fibo_pd(  n - 1  , a );
    }



    QueryPerformanceCounter(&end);
    interval = (double) (end.QuadPart - start.QuadPart) / frequency.QuadPart;

    printf("Tiempo: %f\n", interval);

    printf("%.0Lf\n",res);
}