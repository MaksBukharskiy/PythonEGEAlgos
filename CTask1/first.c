#include <stdio.h>

int main() {
    char choice;

    while (1) {
        printf("Продолжить (y/n): ");
        scanf("%c", &choice);

        if (choice == 'n') {
            break;
        }
        printf("Идём\n");
    }

    return 0;
}