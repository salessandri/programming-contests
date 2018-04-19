#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int columns, i, j, round, length;
static char line[202];

int main() {
    
    scanf("%d", &columns);
    while (columns) {
        scanf("%s", line);
        length = strlen(line);
        for (i = 0; i < columns; i++) {
            round = 0;
            j = i;
            while (j < length) {
                printf("%c", line[j]);
                if (round & 1) {
                    j += 2 * i + 1;
                    round += 1;
                }
                else {
                    j += 2 * columns - (i * 2) - 1;
                    round += 1;
                }
            }
        }
        printf("\n");
        scanf("%d", &columns);
    }
    
    return 0;
}
