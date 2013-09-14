#include <stdio.h>
#include <stdlib.h>

static int tc, x, y, res;

int main() {
    
    scanf("%d", &tc);
    while (tc--) {
        scanf("%d %d", &x, &y);
        res = -1;
        if (x == y) {
            res = 2 * x;
            if (x & 1)
                --res;
        }
        if (x - 2 == y) {
            res = x + y;
            if (x & 1)
                --res;
        }
        if (res == -1)
            printf("No Number\n");
        else
            printf("%d\n", res);
    }
    
    return 0;
}
