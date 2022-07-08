#include<stdio.h>
#include<stdlib.h>
#include "../distr.h"

int main(int argc, char *argv[])
{
	long n = 1000000;
	gaussian("gau1.dat", n);
	gaussian("gau2.dat", n);
	chisqr("chi.dat", n, "gau1.dat", "gau2.dat");
	return 0;
}
