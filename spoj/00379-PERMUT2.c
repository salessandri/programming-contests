#include <stdio.h>
#include <stdlib.h>

static int array[100002], size, i;
static int *p;

int main() {
    
    scanf("%d", &size);
    while (size) {
        p = array + 1;
        for (i = 0; i < size; i++)
            scanf("%d", p++);
        for (i = 1; i <= size && array[array[i]] == i; i++);
        
        if (i > size)
            printf("ambiguous\n");
        else
            printf("not ambiguous\n");
        
        scanf("%d", &size);
    }
    
    return 0;
}
