#include <iostream>

using namespace std;

int main() {
   
    int n,m;
    cin >> n >> m;
    while (n > 0) {
        int matrix[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                cin >> matrix[i][j];
        }
        int tc;
        cin >> tc;
        while (tc--) {
            int from, to;
            cin >> from >> to;
            int i = 0;
            int max_size = 0;
            int limit_col = m-1;
            int limit_row = n;
            int start_index,end_index,j;
            while (i < limit_row) {
                start_index=0;
                end_index=limit_col;
                while (start_index<=end_index) {
                      j=(start_index+end_index)/2;
                    if (matrix[i][j] < from)
                        start_index=j+1;
                    else end_index=j-1;
                }
                if (matrix[i][j]>to) {
                    i++;
                    continue;
                }
                if (matrix[i][j] < from) j++;
                limit_col = j-1;
                while ((j+max_size < m) && (i+max_size < n) && (matrix[i+max_size][j+max_size] <= to))
                    max_size++;
                limit_row = n - max_size;
                i++;
            }
            cout << max_size << endl;
        }
        cout << "-" << endl;
        cin >> n >> m;
    }
   
    return 0;
}
