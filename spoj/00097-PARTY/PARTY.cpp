#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;

typedef pair<int, int> PII;
typedef vector<PII> VPII;

static long long matrix[102][501];
static VPII v_parties;

int main() {
    int budget, parties;
    cin >> budget >> parties;
    while ((budget != 0) && (parties != 0)) {
        v_parties.clear();
        memset(matrix, 0, 501 * 102 * sizeof(long long));
        for (int i = 0; i < parties; i++) {
            int cost, fun;
            cin >> cost >> fun;
            v_parties.push_back(PII(cost, fun));
        }
        for (int i = 1; i <= parties; i++) {
            int cost = v_parties[i-1].first;
            int fun = v_parties[i-1].second;
            for (int j = 1; j <= budget; j++) {
                if (j < cost)
                    matrix[i][j] = matrix[i-1][j];
                else
                    matrix[i][j] = max(matrix[i-1][j], fun + matrix[i-1][j - cost]);
            }
        }
        int ind = budget;
        while (matrix[parties][ind] == matrix[parties][ind-1])
            ind--;
        cout << ind << " " << matrix[parties][ind] << endl;
        cin >> budget >> parties;
    }
}
