#include <algorithm>
#include <iostream>

using namespace std;

struct info {
    char c;
    int from_above;
    int from_left;
    int max_square_size;
    
    info() : from_above(0), from_left(0), max_square_size(0) {}

};

int solve_case() {
    int n;
    cin >> n;
    info matrix[n+1][n+1];
    int result = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; j++) {
            cin >> matrix[i][j].c;
            if (matrix[i][j].c == '.') {
                matrix[i][j].from_above = matrix[i-1][j].from_above + 1;
                matrix[i][j].from_left = matrix[i][j-1].from_left + 1;
                int max_square_size = min(matrix[i][j].from_above, matrix[i][j].from_left);
                matrix[i][j].max_square_size = min(matrix[i-1][j-1].max_square_size + 1, max_square_size);
                result = max(result, matrix[i][j].max_square_size);
            }
        }
    }
    cout << result << '\n';
}

int main() {
    int tests;
    cin >> tests;
    while (tests--) {
        solve_case();
    }
}