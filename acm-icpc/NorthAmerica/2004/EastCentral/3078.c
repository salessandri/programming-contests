#include <stdio.h>
#include <string.h>

static unsigned long long result[5001];
static int i, size;
static char string[50001];

int main() {
    
    scanf("%s", string);
    while (strcmp(string, "0")) {
        size = strlen(string);
        result[size] = 1;
        for (i = size - 1; i >= 0; i--) {
            if (string[i] == '0') {
                result[i] = 0;
                continue;
            }
            result[i] = result[i+1];
            if (((string[i] == '1') && (string[i+1] >= '0')) || ((string[i] == '2') && (string[i+1] >= '0') && (string[i+1] <= '6')))
                result[i] += result[i+2];
        }
        printf("%lld\n", result[0]);
        scanf("%s", string);
    }
    
    return 0;
}
