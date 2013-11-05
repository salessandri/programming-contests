#include <iostream>
#include <cstdio>
#include <stdint.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;



int main() {
	set<unsigned long long> pow2;
	unsigned long long n;
	unsigned long long t;

	for (unsigned long i = 0; i < 64; ++i) {
		pow2.insert((unsigned long long)1 << i);
	}

	cin >> t;
	while (t--) {
		cin >> n;
		if (pow2.find(n+1) != pow2.end())
			cout << "NO\n";
		else
			cout << "YES\n";			
	}
}