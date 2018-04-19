#include <iostream>
#include <cmath>

using namespace std;

int main() {
    unsigned tc;
    cin >> tc;
    while (tc--) {
        unsigned a, b;
        cin >> a >> b;
        a %= 10;
        if (b > 0) {
            unsigned new_b = b % 4;
            b = new_b? new_b : 4;
        }
        cout << (int)pow(a, b) % 10 << endl;
    }
}
