#include <iostream>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

bool my_comp(char* a, char* b) {
    return strcmp(a, b) < 0;
}

typedef map<char*, int, bool(*)(char*,char*)> MSI;

static char array[100000][32];

int main() {
    MSI m(my_comp);
    int tc;
    cin >> tc;
    string line;
    while (tc--) {
        m.clear();
        int n;
        int j = 0;
        cin >> n;
        cin.get();
        for (; j < n; j++) {
            char* raw_line = array[j];
            fgets(raw_line, 35, stdin);
            raw_line[31] = '\0';
            m[raw_line]++;
        }
        for (MSI::iterator it = m.begin(); it != m.end(); it++)
            printf("%s %d\n", it->first, it->second);
        putchar('\n');
    }

}
