#include<stdio.h>
#include<stdlib.h>
#include "../distr.h"

int main()
{
	long n = 1000000;
	double* U = (double*) malloc(n*sizeof(double));
	fillArray("uni.dat", U, n);
	
	printf("Mean = %lf\n",  mean(U,n));
	printf("Variance = %lf\n",  var(U,n));	
	
	free(U);
	return 0;
}
