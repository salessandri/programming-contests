#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<string> line;
    string word;
    int count_char = 0;
    while (cin >> word) {
        if (count_char + line.size() + word.size() > 50) {
            int default_space = 1 + (50 - count_char - line.size()) / (line.size() - 1);
            int
            
    
        }
        else {
            line.push_back(word);
            count_char += word.size();
        }
    }
}
