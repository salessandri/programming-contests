#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;
    int res = n;
    for (int i = 2; i*i <= n; i++)
        res += ((n - i * i) / i) + 1;
    cout << res;
}
