#include <iostream>
#include <string>
#include <map>
#include <stack>
#include <algorithm>
#include <stdio.h>
#include <cmath>
#include <string.h>

using namespace std;

int main(int argc, char** argv)
{
	int cases;
    cin >> cases;
    cin.get();
    for(int i = 1; i <= cases; i++) {
        char c;
        int alt = 0, maxalt = 0;
        c = cin.get();
        while(c != '\n') {
            if(c == '[')
                maxalt = max(maxalt, ++alt);
            else
                alt--;
            c = cin.get();
        }
        cout << i << " " << (int)pow(2, maxalt) << endl;
    }

	return 0;
}
