#include <map>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef map<string, VI> MSVI;

/*bool dist_str(string &a, string &b) {
    
    size_t len_a = a.length();
    size_t len_b = b.length();
    
    if (len_a - len_b > 1)
        return false;
    if (len_a - len_b == 1) {
        return (a.substr(0, len_a-1) == b) || (a.substr(1, len_a-1) == b);
    }
    if (len_b - len_a == 1) {
        return (b.substr(0, len_b-1) == a) || (b.substr(1, len_b-1) == a);
    }
    bool marc = false;
    for (size_t i = 0; i < len_a; i++) {
        if (a[i] != b[i]) {
            if (marc)
                return false;
            else
                return a.substr(i + 1, len_a - i - 1) == b.substr(i + 1, len_a - i - 1);
        }
    }
    return true;
}*/

int main() {
    
    //keys.resize(25000);
    //VVI adjacents;
    //adjacents.resize(25000);
    VI result;
    result.resize(25000);
    MSVI map_strings;
    int size = 0;
    int res = 0, i, j;
    
    while (!cin.eof()) {
        string word;
        cin >> word;
        //keys[size] = word;
        int new_res = 0;
        
        string subword = word.substr(0, word.length()-1);
        if (map_strings.find(subword) != map_strings.end()) {
            for (i = 0; i < map_strings[subword].size(); i++)
                new_res = max(new_res, result[map_strings[subword][i]]);
        }
        
        subword = word.substr(1, word.length()-1);
        if (map_strings.find(subword) != map_strings.end()) {
            for (i = 0; i < map_strings[subword].size(); i++)
                new_res = max(new_res, result[map_strings[subword][i]]);
        }
        
        for (i = 0; i < word.length(); i++) {
            subword = word.substr(0, i-1+1);
            subword += "A";
            subword += word.substr(i+1, word.length()-i-1);
            if (map_strings.find(subword) != map_strings.end()) {
                for (j = 0; j < map_strings[subword].size(); j++)
                    new_res = max(new_res, result[map_strings[subword][j]]);
            }
            map_strings[subword].push_back(size);
        }
        result[size] = ++new_res;
        res = max(res, new_res);
        size++;
    }
    
    cout << res;
    return 0;
}
