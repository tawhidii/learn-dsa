#include <stdio.h>

int main() {
	int a;
	int b;
	a = 20;
	b = 30;
	int *pointer_one;
	int *pointer_two;
	pointer_one = &a;
	pointer_two = &b;
	int sum;
	sum = *pointer_one + *pointer_two;
	// printf("%d\n",a);
	// printf("%p\n",&a);
	printf("%d\n",sum);
	return 0;
}
