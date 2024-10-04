#include <stdio.h>

int main() {
int matrix[3][2] = {{21, 65}, {25, 56}, {54, 22}};  

for (int i = 0; i < 4; i++) {
for (int j = 0; j < 4; j++) {  
printf("%d ", matrix[i][j]);
}
}

return 0;
}