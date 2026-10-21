#include <stdio.h>

struct Date {
    int day;
    int month;
    int year;
};

struct Employee {
    int id;
    char name[24];
    struct Date join_date;
    double salary;
};

void print_employee(const struct Employee *e) {
    printf("ID: %d | Name: %s | Joined: %04d-%02d-%02d | Salary: $%.2f\n",
           e->id, e->name, e->join_date.year, e->join_date.month, e->join_date.day, e->salary);
}

int main(void) {
    struct Employee emp = {1001, "Alice", {15, 6, 2023}, 75000.0};
    print_employee(&emp);
    return 0;
}
