#include <iostream>

using namespace std;

void solve_case() {
    int n, m;
    cin >> n >> m;
    char result;
    if (n <= m) {
        if (n & 1)
            result = 'R';
        else
            result = 'L';
    }
    else {
        if (m & 1)
            result = 'D';
        else
            result = 'U';
    }
    cout << result << '\n';
}

int main() {
    int tests;
    cin >> tests;
    for (int i = 0; i < tests; ++i) {
        solve_case();
    }
}