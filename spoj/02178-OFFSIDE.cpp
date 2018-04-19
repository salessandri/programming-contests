#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    
    unsigned a, d;
    cin >> a >> d;
    while (a != 0) {
        unsigned vec_a[a], vec_d[d];
        for (unsigned i = 0; i < a; i++)
            cin >> vec_a[i];
        for (unsigned i = 0; i < d; i++)
            cin >> vec_d[i];
        sort(vec_a, vec_a+a);
        sort(vec_d, vec_d+d);
        if (vec_a[0] < vec_d[1])
            cout << "Y" << endl;
        else
            cout << "N" << endl;
        cin >> a >> d;
    }
    
    return 0;
}
