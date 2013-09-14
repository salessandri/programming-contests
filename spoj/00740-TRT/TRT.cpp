#include <iostream>
#include <deque>

using namespace std;

typedef deque<int> DI;

int main() {
    
    int n, val, a = 1, result = 0;
    cin >> n;
    DI deq;
    for (int i = 0; i < n; i++) {
        cin >> val;
        deq.push_back(val);
    }
    while (deq.size() > 0) {
        if (deq.front() < deq.back()) {
            result += a * deq.front();
            deq.pop_front();
        }
        else {
            if (deq.back() < deq.front()) {
                result += a * deq.back();
                deq.pop_back();
            }
            else {
                int i = 0, j = deq.size() - 1;
                while ((i < j) && deq[i] == deq[j]) {
                    i++;
                    j--;
                }
                if (deq[i] < deq[j]) {
                    result += a * deq.front();
                    deq.pop_front();
                }
                else {
                    result += a * deq.back();
                    deq.pop_back();
                }
            }
        }
        a++;
    }
    cout << result << endl;
    return 0;
}
