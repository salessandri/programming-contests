#include <iostream>
#include <cstdio>
#include <stdint.h>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define MAX_PAY 100000

uint64_t ways[MAX_PAY];
uint32_t coins[21];

void init() {
    for (int i = 0; i < 21; i++) {
        coins[i] = pow(21 - i, 3);
    }
    ways[0] = 1;
    for (int i = 0; i < 21; i++) {
        uint32_t current_coin = coins[i];
        for (int j = current_coin; j < MAX_PAY; j++) {
            ways[j] = ways[j] + ways[j - current_coin];
        }
    }
}

int main() {
    init();
    int pay;
    while (cin >> pay) {
        cout << ways[pay] << '\n';
    }
    
    return 0;
}