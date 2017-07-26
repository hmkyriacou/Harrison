#include <stdio.h>

int main (){

	float a;
	printf("Insert fist single integer\n");
	scanf("%f", &a);
	float b;
	printf("Insert secound single integer\n");
	scanf("%f", &b);
	int oper;
	printf("Insert operator - '1 = '+',2 = '-',3 = '/',4 = '*''\n");
	scanf("%d", &oper);

		//printf("%d\n", oper);

	switch(oper)
{
		case 1 :
		printf("%f + %f = %f\n", a, b, a+b);
		break;
		case 2 :
		printf("%f - %f = %f\n", a, b, a-b);
		break;
		case 3 :
		//`float result = a/b;
		printf("%f / %f = %f\n", a, b, a/b);
		break;
		case 4 :
		printf("%f * %f = %f\n", a, b, a*b);
		break;
		default :
		printf("invalid operator or numbers\n");
		
}

return 0;
}
