#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>  // needs -lm flag

//functions to find mean and variance, and to load data from a f.dat file
void fillArray(char* filename, double* X, long n);
double mean(double* X,long n);
double var(double* X,long n);
//Contains functions to produce distributions and store them in a .dat file
double sampleGen();
void fillFile(char* filename, double* X, long n);
void uniform(char* filename, long n);
void gaussian(char* filename, long n);
void triangular(char* filename, long n);
void noisy_bernoulli(char* filename, long n, double A, char* Xfilename, char* Nfilename);
void chisqr(char* filename, long n, char* X1file, char* X2file);

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


double sampleGen()
{
	return (double) rand()/RAND_MAX;
}

double bernoulliSampleGen()
{
	return 2*(rand()%2) -1;  //returns -1 or 1
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

// k is half the number of uniform distributions used
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
	double* T = (double*) malloc(n*sizeof(double));
	for(long i=0; i<n;i++)
	{
		T[i]= sampleGen() + sampleGen();
	}
	fillFile(filename, T, n);
	free(T);
	return;
}

void bernoulli(char* filename, long n)
{
	srand(time(NULL));
	double* B = (double*) malloc(n*sizeof(double));
	
	for(long i=0; i<n;i++)
	{
		B[i] = sampleGen() > 0.5 ? 1 : -1 ;
	}
	fillFile(filename, B, n);
	free(B);
	return;
}

//takes output filename, number of samples, files with data for X and N
void noisy_bernoulli(char* filename, long n, double A, char* Xfilename, char* Nfilename)
{
	srand(time(NULL));
	double* Y = (double*) malloc(n*sizeof(double));
	double* X = (double*) malloc(n*sizeof(double));
	double* N = (double*) malloc(n*sizeof(double));
	fillArray(Xfilename, X, n);
	fillArray(Nfilename, N, n);	
	
	for(long i=0; i<n;i++)
	{
		Y[i]= A*X[i] + N[i];
	}
	fillFile(filename, Y, n);
	
	free(Y);
	free(X);
	free(N);
	return;
}

void chisqr(char* filename, long n, char* X1file, char* X2file)
{
	srand(time(NULL));
	double* Y = (double*) malloc(n*sizeof(double));
	double* X1 = (double*) malloc(n*sizeof(double));
	double* X2 = (double*) malloc(n*sizeof(double));
	fillArray(X1file, X1, n);
	fillArray(X2file, X2, n);	
	
	for(long i=0; i<n;i++)
	{
		Y[i]= X1[i]*X1[i] + X2[i]*X2[i];
	}
	fillFile(filename, Y, n);
	
	free(Y);
	free(X1);
	free(X2);
	return;
}
