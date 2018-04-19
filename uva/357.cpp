
#include <iostream>
#include <stdint.h>

#define CANT_COINS 5
#define MAX_CENTS 30001

using namespace std;

uint64_t coins[CANT_COINS] = {50, 25, 10, 5, 1};
uint64_t results[MAX_CENTS] = {0};

void init() {
    uint32_t i, j, c;
    
    results[0] = 1;
    
    for(i = 0; i < CANT_COINS; ++i) {
        c = coins[i];
        for (j = c; j < MAX_CENTS; ++j)
            results[j] += results[j-c];
    }
    
}

int main() {
    int32_t n;
    
    init();
    
    while (cin >> n) {
        uint64_t res = results[n];
        if (res == 1)
            cout << "There is only 1 way to produce " << n << " cents change.\n";
        else
            cout << "There are " << res << " ways to produce " << n << " cents change.\n";
    }
    return 0;
    
}
