#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>

double sampleGen()
{
	return (double) rand()/RAND_MAX;
}

void fillFile(char* filename, long n)
{
	double* V = (double*) malloc(n*sizeof(double));
	for(long i=0; i<n;i++)
	{
		V[i] = -2* log(1-sampleGen());
	}
	
	FILE* fp;
	fp = fopen(filename, "w");
	fwrite(V, sizeof(double), n, fp);
	fclose(fp);
	free(V);
	return;
}

int main()
{
	long n = 1000000;
	fillFile("oth.dat", n);
	return 0;
}
