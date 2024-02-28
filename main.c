#include <stdio.h>

int main() {
	int yearDigits[4];  // The digits of the year as individual integers
	int year;  // The year as a simple integer

	// Get the current year from the user and store it properly in `yearDigits` and `year`
	printf("Enter the year > ");
	scanf("%i", &year);
	yearDigits[3] = year % 10;
	yearDigits[2] = year / 10 % 10;
	yearDigits[1] = year / 100 % 10;
	yearDigits[0] = year / 1000 % 10;
	// And print it back to them
	printf("The year that you entered was %i which has digits %i %i %i %i.\n\n", year, yearDigits[0], yearDigits[1], yearDigits[2], yearDigits[3]);

	// Print out some additional information to the user regarding things that they might need to implement
	printf("Here is a list of the approved operators for they year in which this was written.\n");
	printf("If there is a different set of approved operators this year, you will need to implement the change.\n");
	printf("	1. +	(addition)		(not implemented)\n");
	printf("	2. -	(subtraction/negative)	(not implemented)\n");
	printf("	3. *	(multiplication)	(not implemented)\n");
	printf("	4. /	(division)		(not implemented)\n");
	printf("	5. √	(square root)		(not implemented)\n");
	printf("	6. ^	(exponants)		(not implemented)\n");
	printf("	7. !	(factorial)		(not implemented)\n");
	printf("	8. !!	(double factorial)	(not implemented)\n");
	printf("	9. ()	(parentheses)		(unnecessary to implement)\n\n");

	printf("In addition to the legal operators, the following must be kept in mind:\n");
	printf("	1. Multidigit numbers are legal				(not implemented)\n");
	printf("	2. The negative operator must be implemented separately	(not implemented)\n");
	printf("	3. Decimals are legal					(not implemented)\n");
	printf("	4. 0^0 is equal to 1					(not implemented)\n");
	printf("	5. Use of multidigit numbers should be avoided		(not implemented)\n");
	printf("	6. Keeping the digits in order should be preffered	(not implemented)\n\n");

	return 0;
}
