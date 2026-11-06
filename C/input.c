#include <stdio.h>

int main() {
    float a, b, c;
    double d = 1e-31;

    // Prompt the user for input
    printf("Enter Number 1: ");
    scanf("%f", &a);

    printf("Enter Number 2: ");
    scanf("%f", &b);

    // Perform the calculation
    c = a * b * d * 9.1 / 2;

    // Print the result
    printf("%.10e", c); // Using %.10e for scientific notation with precision

    return 0;
}