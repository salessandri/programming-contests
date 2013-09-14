#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int tc, act_tc, size, i, j;
static char word[83];

int main() {
    
    scanf("%d", &tc);
    for (act_tc = 1; act_tc <= tc; act_tc++) {
        scanf("%d %s", &i, word);
        i--;
        printf("%d ", act_tc);
        size = strlen(word);
        for (j = 0; j < size; j++) {
            if (j == i)
                continue;
            printf("%c", word[j]);
        }
        printf("\n");
    }
    
    return 0;
}
