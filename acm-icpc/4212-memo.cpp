#include <iostream>
#include <algorithm>
#include <stdint.h>
#include <map>

using namespace std;

uint32_t row[100002];
uint32_t max_rows[100002];

uint64_t f(uint32_t* array, uint32_t index, uint32_t size, map<uint32_t, uint64_t>& memo) {
    if (index == size - 1)
      return array[index];
    if (index == size - 2)
      return max(array[index], array[index + 1]);
    if (memo.find(index) != memo.end())
      return memo[index];
    uint64_t tmp = array[index] + f(array, index + 2, size, memo);
    tmp = max(tmp, f(array, index + 1, size, memo));
    memo[index] = tmp;
    return tmp; 
}

int main() {

    uint32_t n, m;
    cin >> m >> n;
    map<uint32_t, uint64_t> memo;
    while (m > 0) {
        for (uint32_t i(0); i < m; ++i) {
            for (uint32_t j(0); j < n; ++j) {
                cin >> row[j];
            }
            memo.clear();
            max_rows[i] = f(row, 0, n, memo);
        }
        memo.clear();
        cout << f(max_rows, 0, m, memo) << '\n';
        cin >> m >> n;
    }
}
