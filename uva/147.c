#include <stdio.h>

#define MAX_AMOUNT 6001
#define COINS_CANT 11
static unsigned int coins[] = {2000, 1000, 400, 200, 100, 40, 20, 10, 4, 2, 1};
static unsigned long long possibilities[MAX_AMOUNT];
static int i, j;
static float cant;

int main() {
    
    /*Initializing*/
    possibilities[0] = 1;
    for (i = 0; i < COINS_CANT; i++) {
        int value = coins[i];
        possibilities[value] = 1;
        for (j = value + 1; j < MAX_AMOUNT; j++) {
            possibilities[j] += possibilities[j-value];
        }
    }
    scanf("%f", &cant);
    while (cant > 0) {
        i = (int)(cant * 20);
        printf("%6.2f%17lld\n", cant, possibilities[i]);
        scanf("%f", &cant);
    }
    
    return 0;
}
