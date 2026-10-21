#include <stdio.h>

static int move_count = 0;

void solve_hanoi(int n, char source, char destination, char auxiliary) {
    if (n == 1) {
        move_count++;
        printf("Move disk 1 from rod %c to rod %c\n", source, destination);
        return;
    }
    solve_hanoi(n - 1, source, auxiliary, destination);
    move_count++;
    printf("Move disk %d from rod %c to rod %c\n", n, source, destination);
    solve_hanoi(n - 1, auxiliary, destination, source);
}

int main(void) {
    int disks = 3;
    printf("Solving Tower of Hanoi for %d disks:\n", disks);
    solve_hanoi(disks, 'A', 'C', 'B');
    printf("Total moves required: %d\n", move_count);
    return 0;
}
