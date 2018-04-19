#include <stdio.h>


static unsigned long long candies, tmp;
static int tc, i, n;

int main() {
    
    scanf("%d", &tc);
    while (tc--) {
        scanf("%d", &n);
        candies = 0;
        i = n;
        while (i--) {
            scanf("%lld", &tmp);
            candies += tmp;
            candies %= n;
        }
        printf("%s\n", (candies == 0)?"YES":"NO");
    }
    
    return 0;
}
