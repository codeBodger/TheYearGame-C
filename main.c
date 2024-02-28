#include <stdio.h>

int main() {
	int yearDigits[4];
	int year;

	printf("Enter the year > ");
	scanf("%i", &year);
	yearDigits[3] = year % 10;
	yearDigits[2] = year / 10 % 10;
	yearDigits[1] = year / 100 % 10;
	yearDigits[0] = year / 1000 % 10;

	printf("The year that you entered was %i which has digits %i %i %i %i.\n\n", year, yearDigits[0], yearDigits[1], yearDigits[2], yearDigits[3]);

	return 0;
}
