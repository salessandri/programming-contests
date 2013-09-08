#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	while (n) {
		int act, ant, i;
		ant = -1;
		for (i = 0; i < n; i++) {
			cin >> act;
			if (act != ant)
				cout << act << " ";
			ant = act;
		}
		cout << "$" << endl;
		cin >> n;
	}
	return 0;
}
