#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main() {
    
    int t;
    cin >> t;
    unsigned long long barns[100000], diff_barns[99999], table[3][99999];
    while (t--) {
        unsigned long long n, c;
        cin >> n >> c;
        memset(table, 0, (n-1) * 3 * sizeof(unsigned long long));
        for (unsigned i = 0; i < n; i++)
            cin >> barns[i];
        sort(barns, barns+n);
        for (unsigned i = 0; i < n - 1; i++) {
            diff_barns[i] = barns[i+1] - barns[i];
        }
        table[0][0] = diff_barns[0];
        for (unsigned i = 1; i < n -1; i++)
            table[0][i] = table[0][i-1] + diff_barns[i];
        unsigned long long *act = table[1], *ant = table[0];
        for (unsigned i = 1; i < c - 1; i++) {
            unsigned j = i;
            act[j-1] = 0;
            while (j < n-1) {
                act[j] = max(act[j-1], min(diff_barns[j], ant[j-1]));
                j++;
            }
            swap(ant, act);
        }
        cout << act[n-2] << endl;
    }
    return 0;
}
