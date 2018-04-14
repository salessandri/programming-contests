#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

void solve_case(int curr_case) {
    int n, p, q;
    cin >> n >> p >> q;
    
    p--; q--;
    int result[p+2][q+2];
    int vec_p[p+1], vec_q[q+1];

    for (int i = 0; i <= p; i++) {
        cin >> vec_p[i];
    }
    for (int i = 0; i <= q; i++) {
        cin >> vec_q[i];
    }
    
    for (int i = 0; i <= p+1; i++)
        result[i][0] = 0;
    for (int j = 0; j <= q+1; j++)
        result[0][j] = 0;
        
    for (int i = 1; i < p+2; i++) {
        for (int j = 1; j < q+2; j++) {
            result[i][j] = 0;
            if (vec_p[i-1] == vec_q[j-1]) {
                result[i][j] = result[i-1][j-1] + 1;
            }
            result[i][j] = std::max(result[i][j], result[i-1][j]);
            result[i][j] = std::max(result[i][j], result[i][j-1]);
        }
    }
    printf("Case %d: %d\n", curr_case, result[p+1][q+1]);

}

int main() 
{
    int cases;
    cin >> cases;
    for (int curr_case = 1; curr_case <= cases; curr_case++) {
        solve_case(curr_case);
    }
    return 0;
}