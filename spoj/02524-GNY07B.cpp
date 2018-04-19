#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main() {

    int n;
    cin >> n;
    for (int tc = 1; tc <= n; tc++) {
        double x;
        string t;
        cin >> x >> t;
        cout << tc << " ";
        if (t == "kg")
            cout << setiosflags(ios::fixed) << setprecision(4) << x * 2.2046 << " lb" << endl;
        else if (t == "lb")
            cout << setiosflags(ios::fixed) << setprecision(4) << x * 0.4536 << " kg" << endl;
        else if (t == "l")
            cout << setiosflags(ios::fixed) << setprecision(4) << x * 0.2642 << " g" << endl;
        else if (t == "g")
            cout << setiosflags(ios::fixed) << setprecision(4) << x * 3.7854 << " l" << endl;
    }

    return 0;
}
