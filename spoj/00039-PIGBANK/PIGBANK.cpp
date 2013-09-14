#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef pair<unsigned long long,unsigned long long> PII;
typedef vector<PII> VPII;

bool my_comp (PII i, PII j) {
    return ((double)i.first / (double)i.second) < ((double)j.first / (double)j.second);
}

unsigned long long val[11000];

int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int e, f, diff;
        cin >> e >> f;
        diff = f - e;
        int coins_cant;
        VPII coins;
        cin >> coins_cant;
        while (coins_cant--) {
            int p, w;
            cin >> p >> w;
            coins.push_back(PII(p, w));
        }
        sort(coins.begin(), coins.end(), my_comp);
        for (int i = 0; i < diff+3; i++)
            val[i] = 999999999;
        for (VPII::iterator it = coins.begin(); it < coins.end(); it++) {
            int i = it->second;
            val[i] = min(val[i], it->first);
            for (i++; i < diff+1; i++)
                val[i] = min(val[i], val[i-(it->second)] + it->first);
        }
        if (val[diff] < 999999999)
            cout << "The minimum amount of money in the piggy-bank is " << val[diff] << "." << endl;
        else
            cout << "This is impossible." << endl;

    }
    return 0;
}
