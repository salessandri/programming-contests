#include <stdio.h>

static int avg, packets[10001], i, n, res;

int main() {
    scanf("%d", &n);
    while (n != -1) {
        avg = 0;
        for (i = 0; i < n; i++) {
            scanf("%d", &packets[i]);
            avg += packets[i];
        }
        if (avg % n != 0) {
            printf("-1\n");
        }
        else {
            res = 0;
            avg /= n;
            for (i = 0; i < n; i++) {
                res += (packets[i] > avg)?(packets[i] - avg) : 0;
            }
            printf("%d\n", res);
        }
        scanf("%d", &n);
    }
    
    return 0;
}
