#include <iostream>
#include <algorithm>

using namespace std;

static unsigned stamps[1001];

int main() {
    unsigned tc;
    cin >> tc;
    for (unsigned i = 1; i <= tc; i++) {
        cout << "Scenario #" << i << ":" << endl;
        int stamps_needed, friends, result;
        int index;
        cin >> stamps_needed >> friends;
        for (int j = 0; j < friends; j++)
            cin >> stamps[j];
        sort(stamps, stamps+friends);
        result = 0;
        index = friends - 1;
        while ((index >= 0) && (stamps_needed > 0)) {
            stamps_needed -= stamps[index--];
            result++;
        }
        if (stamps_needed > 0)
            cout << "impossible" << endl;
        else
            cout << result << endl;
        cout << endl;
    }
}
