#include <stdio.h>
#include <stdlib.h>

static long result;
static int n;

int main() {
    
    scanf("%d", &n);
    while (n) {
        
        result = 0;
        while (n) {
            result += n * n--;
        }
        
        printf("%ld\n", result);
        
        scanf("%d", &n);
    }
    
    return 0;
}
