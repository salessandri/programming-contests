#include <iostream>

using namespace std;

int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int piles;
        cin >> piles;
        int possible_moves = 0;
        for (int i = 1; i <= piles; i++) {
            int tmp;
            cin >> tmp;
            possible_moves += tmp / i;
        }
        if (possible_moves & 1)
            cout << "ALICE" << endl;
        else
            cout << "BOB" << endl;
    }
    return 0;
}
