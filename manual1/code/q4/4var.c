#include<stdio.h>
#include<stdlib.h>
#include "../meanvar.h"

int main()
{
	long n = 1000000;
	double* T = (double*) malloc(n*sizeof(double));
	fillArray("tri.dat", T, n);
	
	printf("Mean = %lf\n",  mean(T,n));
	printf("Variance = %lf\n",  var(T,n));	
	
	free(T);
	return 0;
}
