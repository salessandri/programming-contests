#include <stdio.h>
#include <stdlib.h>

static int stack[1001], stack_size, next, actual, n, i;

int main() {
    stack[0] = 9999;
    scanf("%d", &n);
    while (n) {
        
        next = 1;
        stack_size = 0;
        for (i = 0; i < n; i++) {
            while (stack[stack_size] == next) {
                stack_size--;
                next++;
            }
            scanf("%d", &actual);
            if (actual == next) {
                next++;
                while (stack[stack_size] == next) {
                    stack_size--;
                    next++;
                }
            }
            else {
                stack[++stack_size] = actual;
            }
        }
        
        if (stack_size == 0)
            printf("yes\n");
        else
            printf("no\n");
        scanf("%d", &n);
    }
    
    return 0;
}
