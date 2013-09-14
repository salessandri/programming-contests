#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

typedef multiset<char> MSC;

int main() {
    
    string word_a, word_b;
    while (cin >> word_a >> word_b) {
        MSC s_a, s_b;
        for (string::iterator it = word_a.begin(); it < word_a.end(); it++)
            s_a.insert(*it);
        for (string::iterator it = word_b.begin(); it < word_b.end(); it++)
            s_b.insert(*it);
        char result_set[1001];
        int index = 0;
        for (MSC::iterator it = s_a.begin(); it != s_a.end(); it++) {
            MSC::iterator found_res = s_b.find(*it);
            if (found_res != s_b.end()) {
                s_b.erase(found_res);
                result_set[index++] = *it;
            }
        }
        sort(result_set, result_set+index);
        result_set[index] = '\0';
        cout << result_set << endl;
    }
    return 0;
}
