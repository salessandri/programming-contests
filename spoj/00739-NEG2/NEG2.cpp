#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    string res = "";
    long long n;
    cin >> n;
    if (n == 0) {
        cout << 0 << endl;
        return 0;
    }
    long long min_r, max_r;
    int p = 0;
    min_r = max_r = 0;
    while ((min_r > n) || (max_r < n)) {
        if (p & 1)
            min_r -= pow(2, p);
        else
            max_r += pow(2, p);
        p++;
    }
    while (p-- > 0) {
        long long tmp = pow(-2, p);
        if (tmp < 0)
            if (max_r + tmp < n) {
                res.push_back('0');
                min_r -= tmp;
            }
            else {
                res.push_back('1');
                max_r += tmp;
            }
        else
            if (min_r + tmp > n) {
                res.push_back('0');
                max_r -= tmp;
            }
            else {
                res.push_back('1');
                min_r += tmp;
            }
    }
    cout << res << endl;
    return 0;
}
