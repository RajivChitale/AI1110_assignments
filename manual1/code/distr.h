#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>

// needs -lm flag
//Contains functions to produce distributions and store them in a .dat file

double sampleGen();
void fillFile(char* filename, double* X, long n);
void uniform(char* filename, long n);
void gaussian(char* filename, long n);
void triangular(char* filename, long n);


double sampleGen()
{
	return (double) rand()/RAND_MAX;
}

void fillFile(char* filename, double* X, long n)
{
	FILE* fp;
	fp = fopen(filename, "w");
	fwrite(X, sizeof(double), n, fp);
	fclose(fp);
	return;
}

void uniform(char* filename, long n)
{
	srand(time(NULL));
	double* U = (double*) malloc(n*sizeof(double));
	for(long i=0; i<n;i++)
	{
		U[i]= sampleGen();
	}
	fillFile(filename, U, n);
	free(U);
	return;
}

void gaussian(char* filename, long n)
{
	srand(time(NULL));
	double* X = (double*) malloc(n*sizeof(double));
	for(long j=0; j<n; j++)
	{
		X[j]= -6;
		for(int i=1; i<=12; i++)
		{
			X[j] += sampleGen();
		}
	}
	fillFile(filename, X, n);
	free(X);
	return;
}

void exponential_complement(char* filename, long n)
{
	srand(time(NULL));
	double* V = (double*) malloc(n*sizeof(double));
	for(long i=0; i<n;i++)
	{
		V[i] = -2* log(1-sampleGen());
	}
	fillFile(filename, V, n);
	free(V);
	return;
}

void triangular(char* filename, long n)
{
	srand(time(NULL));
	double* U = (double*) malloc(n*sizeof(double));
	for(long i=0; i<n;i++)
	{
		U[i]= sampleGen() + sampleGen();
	}
	fillFile(filename, U, n);
	free(U);
	return;
}
