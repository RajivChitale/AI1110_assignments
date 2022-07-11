#include<stdio.h>
#include<stdlib.h>
#include <string.h>
#include "../distr.h"

int main(int argc, char *argv[])
{
	double A;
	if(argc==2) {A =  strtod(argv[1], NULL); }
	else {A = 0.5;}
	long n = 1000000;
	gaussianFill("gau.dat", n);
	noisy_bernoulli("max.dat", n, A, "ber.dat", "gau.dat");
	return 0;
}
