#include<stdio.h>
#include<stdlib.h>

//contains functions to find mean and variance, and to load data from a f.dat file

void fillArray(char* filename, double* X, long n);
double mean(double* X,long n);
double var(double* X,long n);

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
	for(long i = 0; i< n; i++)
	{
		mean += X[i]/n;
	}
	return mean;
}

double var(double* X,long n)
{
	double var = 0;
	double m = mean(X,n);
	for(long i = 0; i< n; i++)
	{
		var += (X[i]-m)*(X[i]-m)/n;
	}
	return var;
}

