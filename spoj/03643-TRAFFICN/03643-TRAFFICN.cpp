#include <iostream>
#include <map>
#include <algorithm>
#include <queue>
#include <stdint.h>
#include <stdio.h>

using namespace std;

using namespace std;
 
int const INF = 0x3f3f3f3f;
 
struct state {
    int x, c;
    state() { x = c = 0; }
    state(int _x, int _c)
        : x(_x), c(_c) {}
    bool operator < (const state &s) const {
        return c > s.c;
    }
};

typedef vector<vector<state> > edges_vector;
 
int n, e, k;
bool visited[10000 + 10];
vector<vector<state> > L;
vector<vector<state> > T;
vector<int> d1, d2;
 
vector<int> solve(int src, vector<vector<state> > G, int trg = -1) {
    vector<int> dist(G.size(), INF);
    memset(visited, false, sizeof(visited));
    dist[src] = 0;
    priority_queue<state> q;
    q.push(state(src, 0));
    while (!q.empty()) {
        int indx = q.top().x;
        int cost = q.top().c, i;
        q.pop();
        if (visited[indx]) continue;
        visited[indx] = true;
        if (src == trg) break;
        for (i = 0; i < G[indx].size(); i++) {
            int newc = cost + G[indx][i].c;
            if (newc < dist[G[indx][i].x]) {
                dist[G[indx][i].x] = newc;
                q.push(state(G[indx][i].x, newc));
            }
        }
    }
    return dist;
}
 
int main(int argc, char **argv) {
    int C, src, trg, i, a, b, c; scanf("%d", &C);
    while (C-- != 0) {
        scanf("%d%d%d%d%d", &n, &e, &k, &src, &trg);
        --src, --trg;
        L = vector<vector<state> >(n);
        T = vector<vector<state> >(n);
        for (i = 0; i < e; i++) {
            scanf("%d%d%d", &a, &b, &c);
            L[a - 1].push_back(state(b - 1, c));
            T[b - 1].push_back(state(a - 1, c));
        }
        d1 = solve(src, L);
        d2 = solve(trg, T);
        int res = d1[trg];
        for (i = 0; i < k; i++) {
            scanf("%d%d%d", &a, &b, &c);
            --a, --b;
            res = min(res, d1[a] + c + d2[b]);
            res = min(res, d1[b] + c + d2[a]);
        }
        printf("%d\n", res == INF ? -1 : res);
    }
    return 0;
}