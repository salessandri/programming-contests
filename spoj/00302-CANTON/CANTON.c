#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int solve_quad(int n) {
    
    return (int)(ceil(-0.5 + sqrt(0.25 + 4 * 0.5 * n)));
    
}

static int tc, n, num, base, r;

int main() {
    
    scanf("%d", &tc);
    while (tc--) {
        scanf("%d", &n);
        num = 1;
        r = solve_quad(n);
        base = (r * (r - 1)) / 2 + 1;
        while (base++ != n) {
            num++;
        }
        if (r & 1)
            printf("TERM %d IS %d/%d\n", n, (r + 1) - num, num);
        else
            printf("TERM %d IS %d/%d\n", n, num, (r + 1) - num);
            
    }
    
    return 0;
}
    
    
