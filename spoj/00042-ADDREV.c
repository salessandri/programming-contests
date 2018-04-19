#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static char str_n[22];
static int i, mul, len, tc;
static long long result, n, m;

long long reverse(long long n) {
    
    mul = 1;
    result = 0;
    
    sprintf(str_n, "%lld", n);
    len = strlen(str_n);
    for (i = 0; i < len; i++) {
        result += mul * (str_n[i] - 0x30);
        mul *= 10;
    }

    return result;
}

int main() {
  
    scanf("%d", &tc);
    
    while (tc--) {
        scanf("%lld %lld", &n, &m);
        n = reverse(n);
        m = reverse(m);
        printf("%lld\n", reverse(n + m));
    }
    return 0;
}
