#include <stdio.h>

static unsigned long long result, k;
static unsigned long long array[4] = {192, 442, 692, 942};
static int tc;

int main() {
    
    scanf("%d", &tc);
    while (tc--) {
        scanf("%lld", &k);
        k--;
        result = (k / 4) * 1000;
        result += array[k % 4];
        printf("%lld\n", result);
        
    }
    
    return 0;
}
