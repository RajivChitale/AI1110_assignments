#include<stdio.h>
#include<stdlib.h>

void fillArray(char* filename, double* U, long n)
{
	FILE* fp;
	fp = fopen(filename, "r");
	fread(U, sizeof(double), n, fp);
	fclose(fp);
	return;
}

double mean(double* U,long n)
{
	double mean = 0;
	for(long i = 0; i< n; i++)
	{
		mean += U[i]/n;
	}
	return mean;
}

double var(double* U,long n)
{
	double var = 0;
	double m = mean(U,n);
	for(long i = 0; i< n; i++)
	{
		var += (U[i]-m)*(U[i]-m)/n;
	}
	return var;
}

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
