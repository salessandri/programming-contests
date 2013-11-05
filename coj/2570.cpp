#include <iostream>
#include <cstdio>
#include <stdint.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

	string str_n;
	while (cin >> str_n) {
		int orig_n = atoi(str_n.c_str());
		reverse(str_n.begin(), str_n.end());
		int rev_n = atoi(str_n.c_str());
		if (rev_n > orig_n)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
}