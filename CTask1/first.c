#include "stdio.h"
#include "stdlib.h"

#pragma warning(disable:4996)

int main()
{
    FILE* in = fopen("input.txt", "r");
    FILE* out = fopen("output.txt", "w");

    double c1, c2, c3, b;
    double prev2, prev1, x;

    int count = 0;
    int ok = 1;
 
    fscanf(in, "%lf %lf %lf %lf", &c1, &c2, &c3, &b);

    while (fscanf(in, "%lf", &x) == 1) {

        count++;

        if (count >= 3) {
            long double result = c1 * x + c2 * prev1 + c3 * prev2;

            if (result != b) {
                ok = 0;

            }
        }

        prev2 = prev1;
        prev1 = x;
    }


    if (ok)
        fprintf(out, "да");
    else
        fprintf(out, "нет");


    fclose(in);
    fclose(out);

    return 0;
}
