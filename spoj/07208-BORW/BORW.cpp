#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

typedef pair<int, int> PII;
typedef pair<int, PII> PIPII;
typedef map<PIPII, int> MPIPIII;

static MPIPIII dict;
static int arr[201];
static int n;

int resolv(int i, int min_b, int max_w) {

    PIPII ind(i, PII(min_b, max_w));


    if (dict.find(ind) != dict.end())
        return dict[ind];

    int val;

    if (i == n-1) {
        if ((arr[i] > min_b) || (arr[i] < max_w))
            val = 0;
        else
            val = 1;
    }
    else {

        val = resolv(i+1, min_b, max_w) + 1;
        if (arr[i] > min_b)
            val = min(val, resolv(i+1, arr[i], max_w));
        if (arr[i] < max_w)
            val = min(val, resolv(i+1, min_b, arr[i]));
    }
    dict[ind] = val;
    return val;

}

int main() {

    cin >> n;
    while (n != -1) {
        dict.clear();
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        cout << resolv(0, 0, 2000000) << endl;
        cin >> n;
    }
}
