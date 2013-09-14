#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    
    int n, k, s;
    cin >> n >> k >> s;
    int screws_needed = k * s;
    int screw_boxes[n];
    for (int i = 0; i < n; i++) {
        cin >> screw_boxes[i];
    }
    sort(screw_boxes, screw_boxes+n);
    int cant = 0;
    int index = n - 1;
    while (screws_needed > 0) {
        screws_needed -= screw_boxes[index--];
        cant++;
    }
    cout << cant << endl;
    return 0;
}
