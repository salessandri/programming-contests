#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int max_g = 0;
        int max_mg = 0;
        int cant_g ;
        int cant_mg;
        int tmp;
        cin >> cant_g >> cant_mg;
        while (cant_g--) {
            cin >> tmp;
            max_g = max(max_g, tmp);
        }
        while (cant_mg--) {
            cin >> tmp;
            max_mg = max(max_mg, tmp);
        }
        if (max_g >= max_mg)
            cout << "Godzilla" << endl;
        else
            cout << "MechaGodzilla" << endl;
    }

    return 0;
}
