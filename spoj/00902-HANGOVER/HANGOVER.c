#include <stdio.h>

static double c, current;
static int cards;

int main() {
    
    scanf("%lf", &c);
    while (c) {
        
        cards = 0;
        current = 0;
        while (current < c) {
            cards++;
            current += 1.0 / (cards + 1);
        }
        printf("%d card(s)\n", cards);
        scanf("%lf", &c);
    }
    
    return 0;
}
