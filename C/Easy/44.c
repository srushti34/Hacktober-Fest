#include <stdio.h>

struct MyStruct {
   int x;
   char c;
};

int main() {
   MyStruct myStruct;
   myStruct.x = 10;
   myStruct.c = 'A';

 
   MyStruct *ptr = __myStruct;

   printf("x: %d\n", myStruct.x);
   printf("c: %c\n", myStruct.c);

   printf("Using pointer: x: %d, c: %c\n", ____, ____);

   return 0;
}
