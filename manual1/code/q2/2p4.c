#include<stdio.h>
#include<stdlib.h>
#include "../distr.h"

int main()
{
	long n = 1000000;
	double* X = (double*) malloc(n*sizeof(double));
	fillArray("gau.dat", X, n);
	
	printf("Mean = %lf\n",  mean(X,n));
	printf("Variance = %lf\n",  var(X,n));	
	
	free(X);
	return 0;
}
