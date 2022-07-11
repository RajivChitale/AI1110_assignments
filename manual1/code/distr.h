#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>  // needs -lm flag

//functions to find mean and variance, and to load data from a f.dat file
void fillArray(char* filename, double* X, long n);
void storeArray(char* filename, double* X, long n);
void fillFile(double(*distr)(), char* filename, long n);
double mean(double* X,long n);
double var(double* X,long n);

//Contains functions to produce distributions and store them in a .dat file

double uniform();
void uniformFill(char* filename, long n);

double gaussian();
void gaussianFill(char* filename, long n);

double custom1();
void custom1Fill(char* filename, long n);

double triangular();
void triangularFill(char* filename, long n);

double bernoulli();
void bernoulliFill(char* filename, long n);

double chisqr();
void chisqrFill(char* filename, long n);

double rayleigh();
void rayleighFill(char* filename, long n);

void noisy_bernoulli(char* filename, long n, double A, char* Xfilename, char* Nfilename);

void fillArray(char* filename, double* X, long n)
{
	FILE* fp;
	fp = fopen(filename, "r");
	fread(X, sizeof(double), n, fp);
	fclose(fp);
	return;
}

//takes reference of function
void fillFile(double (*distr) (), char* filename, long n)
{
	FILE* fp;
	fp = fopen(filename, "w");
	srand(time(NULL));
	double* X = (double*) malloc(n*sizeof(double));
	for(long i=0; i<n;i++)
	{
		X[i] =distr();
	}
	fwrite(X, sizeof(double), n, fp);
	free(X);
	fclose(fp);
	return;
}

void storeArray(char* filename, double* X, long n)
{
	FILE* fp;
	fp = fopen(filename, "w");
	fwrite(X, sizeof(double), n, fp);
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

//-------samples of distributions and filling arrays with them -------

//UNIFORM------------------------
double uniform()
{
	return (double) rand()/RAND_MAX;
}

void uniformFill(char* filename, long n)
{
	fillFile(uniform, filename , n);
}

//GAUSSIAN-----------------------
double gaussian()
{
	double g = -6;
	for(int i=1; i<=12; i++)
	{
		g += uniform();
	}
	return g;
}

void gaussianFill(char* filename, long n)
{
	fillFile(gaussian, filename , n);
}


//CUSTOM1----------------------------
double custom1()
{
	return -2* log(1-uniform());
}

void custom1Fill(char* filename, long n)
{
	fillFile(custom1, filename , n);
}

//TRIANGULAR ---------------------------------
double triangular(char* filename, long n)
{
	return uniform() + uniform();
}

void triangularFill(char* filename, long n)
{
	fillFile(triangular, filename , n);
}

//BERNOULLI ---------------------------------
double bernoulli(char* filename, long n)
{
	return uniform() > 0.5 ? 1 : -1 ;
}

void bernoulliFill(char* filename, long n)
{
	fillFile(bernoulli, filename , n);
}


//CHISQR -----------------------------------
double chisqr()
{
	double x1 = gaussian();
	double x2 = gaussian();
	return x1 * x1 + x2 * x2;
}

void chisqrFill(char* filename, long n)
{
	fillFile(chisqr, filename , n);
}

//RAYLEIGH -----------------------------------
double rayleigh(char* filename, long n, char* X1file, char* X2file)
{
	return sqrt(chisqr());
}

void rayleighFill(char* filename, long n)
{
	fillFile(rayleigh, filename , n);
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
	storeArray(filename, Y, n);
	
	free(Y);
	free(X);
	free(N);
	return;
}


