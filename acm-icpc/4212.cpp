#include <iostream>
#include <algorithm>
#include <stdint.h>

using namespace std;

uint32_t row[100002];
uint32_t max_rows[100002];

uint32_t dp(uint32_t* r, uint32_t size) {
    if (size > 1) {
        r[1] = max(r[0], r[1]);
    }
    for (uint32_t i(2); i < size; ++i) {
        r[i] = max(r[i-1], r[i] + r[i-2]);
    }
    return r[size-1];
}

int main() {

    uint32_t n, m;
    cin >> m >> n;
    while (m > 0) {
        for (uint32_t i(0); i < m; ++i) {
            for (uint32_t j(0); j < n; ++j) {
                cin >> row[j];
            }
            max_rows[i] = dp(row, n);
        }
        cout << dp(max_rows, m) << '\n';
        cin >> m >> n;
    }
}
