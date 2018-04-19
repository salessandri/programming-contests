#include <iostream>

using namespace std;

int main() {
	int tc;
	cin >> tc;
	while (tc--) {
		unsigned long long side;
		cin >> side;
		if (side & 1)
			cout << (side * (side + 2) * (2 * side + 1) - 1) / 8 << endl;
		else
			cout << (side * (side + 2) * (2 * side + 1)) / 8 << endl;
	}
	
	
}
