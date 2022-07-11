#include<stdio.h>
#include<stdlib.h>
#include "../distr.h"

int main(int argc, char *argv[])
{
	long n = 1000000;
	rayleighFill("ray.dat", n);
	return 0;
}
