#include <string.h>
#include <stdio.h>

unsigned int lcs[101][101];
char mom[102];
char dad[102];

int main() {
    #memset(lcs, 0, sizeof(unsigned int) * 101 * 101);
    scanf("%s", mom);
    unsigned tc = 1;
    while (mom[0] != '#') {
        scanf("%s", dad);
        unsigned mom_size = strlen(mom);
        unsigned dad_size = strlen(dad);
        for (unsigned i = 1; i <= mom_size; i++) {
            for (unsigned j = 1; j <= dad_size; j++) {
                if (mom[i-1] == dad[j-1])
                    lcs[i][j] = lcs[i-1][j-1] + 1;
                else
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]);
            }
        }
        printf("Case # %i: you can visit at most %i cities.\n",tc++, lcs[mom_size][dad_size]);
        scanf("%s", mom);
    }
}
