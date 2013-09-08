#include <iostream>
#include <string>

using namespace std;


int main() {
	string p1, p2;
	cin >> p1 >> p2;
	while (p1 != "E") {
		int w1, w2;
		w1 = w2 = 0;
		for (unsigned i = 0; i < p1.size(); i++) {
			if ((p1[i] == 'R' && p2[i] == 'S') || (p1[i] == 'S' && p2[i] == 'P') || (p1[i] == 'P' && p2[i] == 'R'))
				w1++;
			if ((p2[i] == 'R' && p1[i] == 'S') || (p2[i] == 'S' && p1[i] == 'P') || (p2[i] == 'P' && p1[i] == 'R'))
				w2++;
		}
		cout << "P1: " << w1 << endl;
		cout << "P2: " << w2 << endl;
		cin >> p1 >> p2;
	}
}
