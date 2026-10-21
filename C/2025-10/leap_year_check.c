#include <stdio.h>

int is_leap_year(int year) {
    if (year % 400 == 0) return 1;
    if (year % 100 == 0) return 0;
    return (year % 4 == 0);
}

int main(void) {
    int test_years[] = {1900, 2000, 2020, 2024, 2025, 2026, 2400};
    int count = sizeof(test_years) / sizeof(test_years[0]);

    for (int i = 0; i < count; i++) {
        int yr = test_years[i];
        printf("Year %d: %s\n", yr, is_leap_year(yr) ? "LEAP YEAR" : "COMMON YEAR");
    }
    return 0;
}
