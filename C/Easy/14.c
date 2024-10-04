#include <stdio.h>

struct person {
    char name[20];
    int age;
};

void display(struct person p);

int main() {
    struct person p1;
    printf("Enter name: ");
    scanf("%s", p1.name);
    printf("Enter age: ");
    scanf("%d", p1.age);
    display(p1);
    return 0;
}

void display(struct person p) {
    printf("Name: %s, Age: %d\n", p.name, p.age);
}