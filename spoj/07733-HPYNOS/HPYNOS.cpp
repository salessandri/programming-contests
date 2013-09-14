#include <iostream>
#include <set>

using namespace std;

int main() {
    unsigned int x;
    cin >> x;
    set<unsigned int> processed;
    int count = 0;
    while ((x != 1) && (processed.find(x) == processed.end())) {
        count += 1;
        processed.insert(x);
        unsigned int new_x(0), dig;
        while (x) {
            dig = x % 10;
            new_x += dig * dig;
            x /= 10;
        }
        x = new_x;
    }
    if (x == 1)
        cout << count << endl;
    else
        cout << -1 << endl;
    return 0;
}
