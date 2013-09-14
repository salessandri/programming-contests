#include <stdio.h>
#include <stdlib.h>

static int n[1002], m[1002];
static int size, i, tc, result;

int compare(const void *_a, const void *_b) {
 
        int *a, *b;
        
        a = (int *) _a;
        b = (int *) _b;
        
        return (*a - *b);
}


int main() {
    
    scanf("%d", &tc);
    while (tc--) {
        
        scanf("%d", &size);
        
        for (i = 0; i < size; i++)
            scanf("%d", &n[i]);
        
        for (i = 0; i < size; i++)
            scanf("%d", &m[i]);
        
        qsort(n, size, sizeof(int), &compare);
        qsort(m, size, sizeof(int), &compare);
        
        result = 0;
        for (i = 0; i < size; i++) {
            result += n[i] * m[i];
        }
        
        printf("%d\n", result);
        
    }
    
    return 0;
}
