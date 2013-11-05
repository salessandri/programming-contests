#include <iostream>
#include <cstdio>
#include <stdint.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct point {
    int height;
    int x;
    int y;
    
    point(int x_, int y_, int h_) : height(h_), x(x_), y(y_) {}
    
};

bool operator<(const point a, const point b) {
    return a.height < b.height;
}

void process_case() {
    string casename;
    int r, c;
    cin >> casename >> r >> c;
    int grid[r][c];
    int partial_result[r][c];
    vector<point> heap;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> grid[i][j];
            partial_result[i][j] = 1;
            point p(i, j, grid[i][j]);
            heap.push_back(p);
        }
    }
    sort(heap.begin(), heap.end());
    int result = 0;
    for (vector<point>::const_iterator it = heap.begin(); it != heap.end(); it++) {
        int i = it->x;
        int j = it->y;
        if (i > 0 && grid[i][j] > grid[i-1][j])
            partial_result[i][j] = max(partial_result[i][j], partial_result[i-1][j]+1);
        if (i < r-1 && grid[i][j] > grid[i+1][j])
            partial_result[i][j] = max(partial_result[i][j], partial_result[i+1][j]+1);
        if (j > 0 && grid[i][j] > grid[i][j-1])
            partial_result[i][j] = max(partial_result[i][j], partial_result[i][j-1]+1);
        if (j < c-1 && grid[i][j] > grid[i][j+1])
            partial_result[i][j] = max(partial_result[i][j], partial_result[i][j+1]+1);
        result = max(result, partial_result[i][j]);
    }

    printf("%s: %d\n", casename.c_str(), result);
    
}

int main() {
    
    int test_cases;
    
    cin >> test_cases;
    for (int i = 0; i < test_cases; ++i) {
        process_case();
    }
    
    return 0;
}