#include<stdio.h>
#include<stdlib.h>
#include<time.h>

double sampleGen()
{
	return (double) rand()/RAND_MAX;
}

void fillFile(char* filename, long n)
{
	double* X = (double*) malloc(n*sizeof(double));
	for(long j=0; j<n; j++)
	{
		X[j]= -6;
		for(int i=1; i<=12; i++)
		{
			X[j] += sampleGen();
		}
	}
	
	FILE* fp;
	fp = fopen(filename, "w");
	fwrite(X, sizeof(double), n, fp);
	fclose(fp);
	free(X);
	return;
}

int main()
{
	long n = 1000000;
	fillFile("gau.dat", n);
	return 0;
}
