#include <stdio.h>

void try_modify(int val) {
    val += 100;
    printf("Inside try_modify: val = %d\n", val);
}

int calculate_cylinder_volume(int radius, int height, double *vol) {
    if (radius <= 0 || height <= 0) return 0;
    const double PI = 3.141592653589793;
    *vol = PI * radius * radius * height;
    return 1;
}

int main(void) {
    int original = 50;
    printf("Before call: original = %d\n", original);
    try_modify(original);
    printf("After call : original = %d (call by value unchanged)\n", original);

    double volume = 0.0;
    if (calculate_cylinder_volume(4, 10, &volume)) {
        printf("Cylinder (r=4, h=10) Volume = %.2f\n", volume);
    }
    return 0;
}
