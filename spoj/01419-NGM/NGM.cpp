#include <iostream>

using namespace std;

int main() {
    unsigned long long n;
    cin >> n;
    unsigned l_d = n % 10;
    if (l_d)
        cout << 1 << endl << l_d << endl;
    else
        cout << 2 << endl;
}
