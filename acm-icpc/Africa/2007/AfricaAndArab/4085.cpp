#include <iostream>
#include <string>

using namespace std;

int main() {
	int tc = 1;
	string num;
	cin >> num;
	while (num != "0") {
		string res;
		string::reverse_iterator rit = num.rbegin();
		int last_dig_mult = 0;
		int last_dig_orig;
		int carry = 0;
		while (rit != num.rend()) {
			last_dig_orig = ((*rit) - 0x30) - last_dig_mult - carry;
			if (last_dig_orig < 0) {
				carry = 1;
				last_dig_orig += 10;
			}
			else {
				carry = 0;
			}
			last_dig_mult = last_dig_orig;
			res.insert(res.begin(), (char)last_dig_orig + 0x30);
			rit++;
		}
		cout << tc++ << ". ";
		if (res.at(0) ==  '0')
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
		cin >> num;
	}
	
	return 0;
}
