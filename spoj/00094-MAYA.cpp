#include <iostream>

using namespace std;

int table[] = {1, 20, 360, 7200, 144000, 2880000, 57600000};

int main() {

    int n;
    unsigned long long res;
    cin >> n;
    while (n) {
        cin.get();
        res = 0;
        while (n--) {
            int dig = 0;
            char c = cin.get();
            while (c != '\n') {
                switch (c) {
                    case '.':
                        dig++;
                        break;
                    case '-':
                        dig += 5;
                }
                c = cin.get();
            }
            res += table[n] * dig;
        }
        cout << res << endl;
        cin >> n;
    }

    return 0;
}
