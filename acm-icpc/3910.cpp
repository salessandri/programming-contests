#include <iostream>
#include <string>
using namespace std;

int main(int argc, char** argv)
{
	string line;
    int cases;
    int n;
    
    cin >> cases;
    for (int caso = 1; caso <= cases; caso++) {
        cin >> n;
        cin >> line;
        line.erase(line.begin() + n - 1);
        cout << caso << " " << line << endl;
    }
	return 0;
}
