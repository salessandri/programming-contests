#include <iostream>

using namespace std;

int main() {
	int i,j,k;
	int n;
	cin >> n;
	cout << "Gnomes:" << endl;
	while (n--) {
		cin >> i >> j >> k;
		if (((i < j) && (j < k)) || ((i > j) && (j > k)))
			cout << "Ordered" << endl;
		else
			cout << "Unordered" << endl;
	}
}
