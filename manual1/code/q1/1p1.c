#include<stdio.h>
#include<stdlib.h>
#include<time.h>

double sampleGen()
{
	return (double) rand()/RAND_MAX;
}

void fillFile(char* filename, long n)
{
	double* U = (double*) malloc(n*sizeof(double));
	for(long i=0; i<n;i++)
	{
		U[i]= sampleGen();
	}
	
	FILE* fp;
	fp = fopen(filename, "w");
	fwrite(U, sizeof(double), n, fp);
	fclose(fp);
	free(U);
	return;
}

int main()
{
	long n = 1000000;
	fillFile("uni.dat", n);
	return 0;
}
