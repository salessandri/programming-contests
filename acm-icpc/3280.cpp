#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct Item {
    string str;
    int i;
    
    bool operator< (const Item &it) const {
        return str < it.str;
    }
};

static string words[101], abbrev[101];
static Item sortedWords[101];
static int nWords;

inline int lengthForWord(int i, int min) {
    if(i == nWords - 1) {
        abbrev[sortedWords[i].i] = sortedWords[i].str.substr(0, min);
        return min;
    }
    else {
        int index = 0;
        while(index < sortedWords[i].str.size() && index < sortedWords[i+1].str.size() && sortedWords[i].str[index] == sortedWords[i+1].str[index]) {
            index++;
        }
        if(index < min) {
            abbrev[sortedWords[i].i] = sortedWords[i].str.substr(0, min);
        }
        else
            abbrev[sortedWords[i].i] = sortedWords[i].str.substr(0, index + 1);
        return index + 1;
    }
}

void calculate() {
    int min = 1;
    for(int i = 0; i < nWords; i++) {
        min = lengthForWord(i, min);
    }
}

int main() {
    int nCase = 1; 
    cin >> nWords;
    while(nWords) {
        for(int i = 0; i < nWords; i++) {
            cin >> words[i];
            sortedWords[i].str = words[i];
            sortedWords[i].i = i;
        }
        sort(&sortedWords[0], &sortedWords[nWords]);
        
        calculate();
        
        cout << nCase << endl;
        for(int i = 0; i < nWords; i++)
            cout << words[i] << " " << abbrev[i] << endl;
        
        cin >> nWords;    
        nCase++;
    }
}
