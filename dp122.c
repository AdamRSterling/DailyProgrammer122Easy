#include <stdio.h>

int findDigitalRoot(number)
{
	while(number >= 10)
		number = number % 10 + findDigitalRoot(number / 10);
	return number;
}

int main(int argc, char *argv[])
{
	int digitalRoot = findDigitalRoot(atoi(argv[1]));
	printf("Digital root: %d", digitalRoot);
	return 0;
}