#include <iostream>
#include <map>
#include <algorithm>
#include <queue>
#include <stdint.h>
#include <stdio.h>

using namespace std;

int32_t heights[10001];
int32_t in_grad[10001];

int main() {
    
    int32_t n, tmp, i;
    int32_t x, max_x, result;
    cin >> n;
    while (n > -1) {
        vector<int32_t> tree[n];
        deque<int32_t> visited;
        
        result = -1;
        
        for (i = 0; i < n; ++i) {
            heights[i] = -1;
            in_grad[i] = 0;
        }
        
        for (i = 1; i < n; ++i) {
            cin >> tmp;
            tmp--;
            tree[i].push_back(tmp);
            tree[tmp].push_back(i);
            in_grad[i]++;
            in_grad[tmp]++;
        }
        
        for (i = 0; i < n; ++i) {
            if (in_grad[i] == 1) {
                visited.push_back(i);
            }
        }
        
        while (visited.size()) {
            x = visited.front();
            visited.pop_front();
            max_x = -10;
            for (vector<int32_t>::iterator it = tree[x].begin(); it != tree[x].end(); it++) {
                tmp = *it;
                max_x = max(max_x, heights[tmp]);
                in_grad[tmp]--;
                if (in_grad[*it] == 1) {
                    visited.push_back(tmp);
                }
            }
            heights[x] = max_x + 1;
            result = max(result, max_x + 1);
            
        }
        
        printf("%d\n", result);
        cin >> n;
        
    }
    
    return 0;
}
