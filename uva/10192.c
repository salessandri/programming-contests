#include <string.h>
#include <stdio.h>

int main() {
    unsigned int lcs[101][101];
    char mom[102];
    char dad[102];
    memset(lcs, 0, sizeof(unsigned int) * 101 * 101);
    gets(mom);
    unsigned tc = 1;
    while (mom[0] != '#') {
        unsigned i, j;
        unsigned mom_size = strlen(mom);
        unsigned dad_size;
        gets(dad);
        dad_size = strlen(dad);
        for (i = 1; i <= mom_size; i++) {
            for (j = 1; j <= dad_size; j++) {
                if (mom[i-1] == dad[j-1])
                    lcs[i][j] = lcs[i-1][j-1] + 1;
                else
                    lcs[i][j] = (lcs[i-1][j] > lcs[i][j-1])?(lcs[i-1][j]):(lcs[i][j-1]);
            }
        }
        printf("Case #%i: you can visit at most %i cities.\n",tc++, lcs[mom_size][dad_size]);
        gets(mom);
    }
    return 0;
}
