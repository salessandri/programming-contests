#include <iostream>
#include <vector>
#include <list>
#include <set>

using namespace std;

typedef list<int> VI;
typedef vector<VI> VVI;
typedef set<int> SI;

bool set_off(VVI &graph, SI &visited, int i) {
    
    visited.insert(i);
    for (VI::iterator it = graph[i].begin(); it != graph[i].end(); it++) {
        graph[*it].remove(i);
        if (visited.find(*it) != visited.end()) {
            return false;
        }
        if (!set_off(graph, visited, *it)) {
            return false;
        }
    }
    return true;
    
}

int main() {
    
    unsigned n, m;
    cin >> n >> m;
    VVI graph(n+1);
    SI visited;
    if (m != n-1) {
        cout << "NO" << endl;
        return 0;
    }
    while (m--) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    bool ok = true;
    ok = set_off(graph, visited, 1);
    if (ok && (visited.size() == n))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}
