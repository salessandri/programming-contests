#include <stdio.h>
#include <stdlib.h>

static int tc, i;
static long long n;
static long result;
static long long divisor;

int main() {
    
    scanf("%d", &tc);
    for (i = 0; i < tc; i++) {
        scanf("%lld", &n);
        result = 0;
        divisor = 5;
        while (divisor <= n) {
            result += n / divisor;
            divisor *= 5;
        }
        printf("%ld\n", result);
    }
    
    return 0;
}
