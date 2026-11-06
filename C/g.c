#include<stdio.h> 

int main() {
    float a, b, c;
    double d = 1e-31;

    printf("Enter Number 1: ");
    scanf("%f", &a);

    printf("enter number 2: ");
    scanf("%f", &b);

   c = a * b;
   printf("%f", c);
   return 0;
}