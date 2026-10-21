#include <stdio.h>
#include <string.h>

struct Item {
    char name[20];
    int quantity;
    double price;
};

void print_inventory(const struct Item items[], int count) {
    double grand_total = 0.0;
    printf("%-15s %8s %10s %10s\n", "Item Name", "Qty", "Price", "Total");
    printf("--------------------------------------------\n");
    for (int i = 0; i < count; i++) {
        double total = items[i].quantity * items[i].price;
        grand_total += total;
        printf("%-15s %8d %10.2f %10.2f\n", items[i].name, items[i].quantity, items[i].price, total);
    }
    printf("--------------------------------------------\n");
    printf("Grand Total: $%.2f\n", grand_total);
}

int main(void) {
    struct Item inventory[] = {
        {"Keyboard", 5, 49.99},
        {"Mouse", 12, 19.50},
        {"Monitor", 3, 179.00}
    };
    print_inventory(inventory, 3);
    return 0;
}
