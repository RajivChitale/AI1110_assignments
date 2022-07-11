#include<stdio.h>
#include<stdlib.h>
#include "../distr.h"

int main(int argc, char *argv[])
{
	long n = 1000000;
	chisqrFill("chi.dat", n);
	return 0;
}
