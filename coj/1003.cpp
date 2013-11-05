#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void solve_case() {
    int n, m;
    cin >> n >> m;
    vector<int> votes(n, 0);
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int tmp;
            cin >> tmp;
            votes[j] += tmp;
        }
    }
    int winner = 0;
    for (int j = 1; j < n; ++j) {
        if (votes[j] > votes[winner])
            winner = j;
    }
    cout << winner+1 << '\n';
}

int main() {
    int tests;
    cin >> tests;
    for (int i = 0; i < tests; ++i) {
        solve_case();
    }
}