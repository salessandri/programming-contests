#include <stdio.h>
#include <stdlib.h>

static int divisors[500001];
static int tc, i, j;

int main() {
    
    for (i = 1; i < 500000; i++) {
        for (j = i * 2; j < 500001; j += i) {
            divisors[j] += i;
        }
    }
    
    scanf("%d", &tc);
    while (tc--) {
        scanf("%d", &i);
        printf("%d\n", divisors[i]);
    }
    return 0;
}
