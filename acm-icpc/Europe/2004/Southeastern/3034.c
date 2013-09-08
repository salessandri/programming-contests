#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int solve_quad(int n) {
    
    return (int)(ceil(-0.5 + sqrt(0.25 + 4 * 0.5 * n)));
    
}

static int tc, n, num, base, r;

int main() {
    
    tc = scanf("%d", &n);
    while (tc != EOF) {
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
        
        tc = scanf("%d", &n);
        
    }
    
    return 0;
}
    
    
