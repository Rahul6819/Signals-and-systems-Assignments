include <stdio.h>

// Function to generate arithmetic progression and save to file
void generate_arithmetic_progression(int a, int d, int n) {
    FILE *fp;
    fp = fopen("data3.txt", "w");
    if (fp == NULL) {
        printf("Error opening the file.\n");
        return;
    }

    // Generate and write the arithmetic progression values to file
    for (int i = 0; i < n; i++) {
        fprintf(fp, "%d\n", a + i*d);
    }
    fclose(fp);
}

int main() {
    // Parameters for the arithmetic progression
    int a = 5;  // initial term
    int d = 3/2;  // common difference
    int n = 30; // number of terms

    // Generate the arithmetic progression and save to file
    generate_arithmetic_progression(a, d, n);

    return 0;
}