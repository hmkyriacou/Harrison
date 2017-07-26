#include <stdio.h>

int main (){
	int x;
	printf("Enter Number\n");
	x = get();
	if (x%2 == 0)
		printf("%d is even\n", x-48);
	else
		printf("%d is odd\n", x-48);
return 0;
}
