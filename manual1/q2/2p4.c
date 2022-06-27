#include<stdio.h>
#include<stdlib.h>

void fillArray(char* filename, double* X, long n)
{
	FILE* fp;
	fp = fopen(filename, "r");
	fread(X, sizeof(double), n, fp);
	fclose(fp);
	return;
}

double mean(double* X,long n)
{
	double mean = 0;
	for(long j = 0; j< n; j++)
	{
		mean += X[j]/n;
	}
	return mean;
}

double var(double* X,long n)
{
	double var = 0;
	double m = mean(X,n);
	for(long j = 0; j< n; j++)
	{
		var += (X[j]-m)*(X[j]-m)/n;
	}
	return var;
}

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
