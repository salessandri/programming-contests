#include <iostream>
#include <deque>

using namespace std;

typedef pair<int, int> PII;
typedef deque<PII> DPII;

int main() {
    
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        
        
        int i, j, total;
        string line;
        DPII queue;
        cin >> n;
        cin >> m;
        unsigned long long result[n][m];
        bool visited[n][m];
        
        for (i = 0; i < n; i++) {
            cin >> line;
            for (j = 0; j < m; j++) {
                visited[i][j] = false;
                if (line[j] == '1') {
                    queue.push_back(PII(i, j));
                }
            }
        }
        queue.push_back(PII(-1, -1));
        i = 0;
        j = 0;
        total = n * m;
        while (j < total) {
            PII first = queue.front();
                        
            queue.pop_front();
            if (first.first == -1) {
                queue.push_back(first);
                i++;
                continue;
            }
            if (visited[first.first][first.second])
                continue;
            visited[first.first][first.second] = true;
            j++;
            result[first.first][first.second] = i;
            if (first.first > 0)
                queue.push_back(PII(first.first-1, first.second));
            if (first.first < n-1)
                queue.push_back(PII(first.first+1, first.second));
            if (first.second > 0)
                queue.push_back(PII(first.first, first.second-1));
            if (first.second < m-1)
                queue.push_back(PII(first.first, first.second+1));
        }
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
                cout << result[i][j];
                if (j < m-1)
                    cout << ' ';
            }
            cout << endl;
        }
    }
    
    return 0;
}
