
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static unsigned char sc[2];
static char names[2][21];
static char choice[5];
static int i, n ,m1, m2;

int main(int argc, char** argv)
{
	scanf("%s %s %s", names[0], names[1], choice);
    while (strcmp(choice, "#") != 0) {
        sc[0] = sc[1] = 0;
        scanf("%d", &i);
        while (i--) {
            scanf("%d", &n);
            ++sc[n % 2];
        }
        m1 = strcmp("even", choice) == 0? 1 : 0;
        m2 = strcmp("even", choice) == 0? 0 : 1;
        printf("%s %d %s %d\n", names[0], sc[m1], names[1], sc[m2]);
        scanf("%s %s %s", names[0], names[1], choice);
    }
	return 0;
}
