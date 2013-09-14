#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n, r, tc = 1;
    int cant_needed
    cin >> n >> r;
    while (n  && r) {
        cant_needed = ceil((float)n / r);
        if (cant_needed > 27)
            cout << "Case " << tc++ << ": impossible\n";
        else
            cout << "Case " << tc++ << ": " << --cant_needed << "\n";
        cin >> n >> r;
    }
}
