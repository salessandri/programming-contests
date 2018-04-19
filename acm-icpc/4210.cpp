#include <stdint.h>
#include <iostream>
#include <cstring>
#include <queue>
#include <vector>

#define INF 99999999

using namespace std;

uint32_t arcs[500 * 500];
uint32_t rarcs[500 * 500];

struct my_pair {
    
    uint32_t u;
    uint32_t p;
    
    bool operator<(const my_pair& other) const{
        return this->p >= other.p;
    }
};

vector<uint32_t> dijkstra(uint16_t init, uint16_t size, uint32_t* matrix) {
    priority_queue<my_pair> queue;
    vector<uint32_t> result(size, INF);
    bool used[size];
    my_pair working, working2;
    uint32_t i, dist;
    
    for (i = 0; i < size; ++i)
        used[i] = false;
    
    result[init] = 0;
    
    working.u = init;
    working.p = 0;
    queue.push(working);
    while (!queue.empty()) {
        working = queue.top();
        queue.pop();
        
        if (used[working.u])
            continue;
        used[working.u] = true;
        
        for (i = 0; i < size; i++) {
            dist = matrix[working.u * size + i];
            if (result[working.u] + dist < result[i]) {
                result[i] = result[working.u] + dist;
                working2.u = i;
                working2.p = result[working.u] + dist;
                queue.push(working2);
            }
        }
    }
    return result;
    
}

int main() {
    
    uint32_t n, m;
    uint32_t i;
    uint32_t s, d;
    uint32_t u, v, p;
    vector<uint32_t> res_d1, res_d2, res_d3;
    
    cin >> n >> m;
    while (n != 0) {
        
        for (i = 0; i < n * n; ++i) {
            arcs[i] = INF;
            rarcs[i] = INF;
        }
        
        cin >> s >> d;
        
        for (i = 0; i < m; ++i) {
            cin >> u >> v >> p;
            arcs[u * n + v] = p;
            rarcs[v * n + u] = p;
        }
        
        res_d1 = dijkstra(s, n, arcs);
        res_d2 = dijkstra(d, n, rarcs);
        
        uint32_t min_path = res_d1[d];
        if (min_path == INF) {
            cout << -1 << '\n';
            continue;
        }
        
        /* Delete arcs that are part of a shortest path */
        for (u = 0; u < n; ++u) {
            for (v = 0; v < n; ++v) {
                uint32_t dist = arcs[u * n + v];
                if (res_d1[u] + dist + res_d2[v] == min_path) {
                    arcs[u * n + v] = INF;
                }
            }
        }
        
        res_d3 = dijkstra(s, n, arcs);
        if (res_d3[d] == INF)
            cout << -1 << '\n';
        else
            cout << res_d3[d] << '\n';
        cin >> n >> m;
    }
    
    return 0;
}
