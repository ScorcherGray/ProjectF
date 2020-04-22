template factorial(int n)
{
   enum { factorial = n* .factorial!(n-1) }
}

template factorial(int n : 1)
{
   enum { factorial = 1 }
}

int main() {
   printf("%d\n", factorial!(4));	// prints 24
   return 0;
}

