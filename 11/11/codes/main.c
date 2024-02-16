/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main() {
    FILE *fp;
    int a = 3;  // first term
    int r = 3;  // common ratio
    int n = 15;  // number of terms

    // Calculate the terms of the G.P. and write to file
    fp = fopen("terms.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        int term = a * pow(r, i);
        fprintf(fp, "%d\n", term);
    }

    fclose(fp);
    return 0;
}
