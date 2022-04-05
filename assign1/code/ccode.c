#include<stdio.h>
#include<stdlib.h>

struct MyMatrix
{
	int rows;
	int cols;
	int* arr;
};
typedef struct MyMatrix Matrix;

		/* function declarations */

Matrix Matrix_dot(Matrix left, Matrix right);			//dot product

Matrix Matrix_scalar(Matrix inpm, int k);				//scalar multiplication 

Matrix Matrix_add(Matrix left, Matrix right);			//addition 

Matrix Matrix_sub(Matrix left, Matrix right);			//subtraction

Matrix Matrix_fill(int rows, int cols, int inparr[]);	//fill values in matrix

void Matrix_print(Matrix m);							//print values from matrix


int main()
{	
	int data_B[] = {1,1,	8,3};
	Matrix B = Matrix_fill(2, 2, data_B);  //initialize matrix B
	
	int data_Sol[] = {1,10};
	Matrix Sol = Matrix_fill(2, 1, data_Sol); //initialize vector with solutions for a,b
	
	int data_R[] = {5,50};
	Matrix R = Matrix_fill(2, 1, data_R); //initialize vector on RHS

	Matrix Bsqr = Matrix_dot(B,B);
	Matrix Bfour = Matrix_scalar(B, 4);
	Matrix X= Matrix_sub(Bsqr, Bfour); 	//calculate matrix X
	Matrix L= Matrix_dot(X, Sol);	 	//calculate LHS
	
	printf("Matrix X =\n");
	Matrix_print(X);
	printf("\nVerifying whether LHS=RHS for a=1, b=10,\n");
	printf("LHS =\n");
	Matrix_print(L);
	printf("\nRHS =\n");
	Matrix_print(R);
	
	free(B.arr);		//free memory from heap
	free(Sol.arr);
	free(R.arr);
	free(Bsqr.arr);
	free(Bfour.arr);
	free(X.arr);
	free(L.arr);
	return 0;
}

			/* function definitions */

//dot product: takes in two matrices and returns their dot product
Matrix Matrix_dot(Matrix left, Matrix right)
{
	if(left.cols!=right.rows)
	{
		printf("Matrix incompatible for dot product\n"); return left;
	}
	
	Matrix m;
	m.rows = left.rows;
	m.cols = right.cols;	
	m.arr = malloc(sizeof(int) * m.rows * m.cols);	
	
	int tempsum;
	
	for(int y=0; y< m.rows; y++)
	{
		for(int x=0; x< m.cols; x++)
		{
			tempsum=0;
			for(int i=0; i<left.cols; i++)
			{
				tempsum += left.arr[i+ y*left.cols] * right.arr[x+ i*right.cols];
			}
			m.arr[x+ y*(m.cols)] = tempsum;
		}
	}
	return m;
}

//scalar multiplcation: takes in a matrix and integer. Returns the result of their scalar multiplication 
Matrix Matrix_scalar(Matrix inpm, int k)
{
	Matrix m;
	m.rows= inpm.rows;
	m.cols= inpm.cols;	
	int size = m.rows * m.cols;
	m.arr = malloc(sizeof(int) * size);
	
	for(int i=0; i< size; i++)
	{
		m.arr[i]= k * inpm.arr[i];
	}
	return m;
}

//addition: takes in two matrices, returns their sum
Matrix Matrix_add(Matrix left, Matrix right)
{
	if( (left.rows!=right.rows) || (left.cols!=right.cols) )
	{
		printf("Matrix incompatible for addition\n"); return left;
	}
	
	Matrix m;
	int index;
	m.rows=left.rows;
	m.cols=left.cols;
	m.arr = malloc(sizeof(int) * m.rows * m.cols);
	
	for(int y=0; y< m.rows; y++)
	{
		for(int x=0; x< m.cols; x++)
		{
			index= x+ y*(m.cols);
			m.arr[index] = left.arr[index] + right.arr[index];
		}
	}
	return m;
}

//subtraction: takes in two matrices, returns their difference (left-right)
Matrix Matrix_sub(Matrix left, Matrix right)
{
	if( (left.rows!=right.rows) || (left.cols!=right.cols) )
	{
		printf("Matrix incompatible for addition\n"); return left;
	}
	
	Matrix m;
	int index;
	m.rows=left.rows;
	m.cols=left.cols;
	m.arr = malloc(sizeof(int) * m.rows * m.cols);
	
	for(int y=0; y< m.rows; y++)
	{
		for(int x=0; x< m.cols; x++)
		{
			index= x+ y*(m.cols);
			m.arr[index] = left.arr[index] - right.arr[index];
		}
	}
	return m;
}

//takes in number of rows, columns and elements (in row major order). Uses them to create and return a matrix.
Matrix Matrix_fill(int rows, int cols, int inparr[])
{	
	Matrix m;
	m.rows = rows;
	m.cols = cols;
	m.arr = malloc(rows*cols*sizeof(int));
	
	for(int i=0; i< rows*cols; i++)
	{
		m.arr[i]=inparr[i];
	}
	return m;
}

//takes in matrix m, prints its elements
void Matrix_print(Matrix m)
{
	for(int y=0; y< m.rows; y++)
	{
		for(int x=0; x< m.cols; x++)
		{
			printf("%d ", m.arr[x+ y*(m.cols)] ); 
		}
		printf("\n");
	}	
	return;
}

