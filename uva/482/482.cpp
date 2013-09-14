#include <iostream>
#include <vector>
#include <string>
#include <sstream>



using namespace std;

typedef vector<unsigned> VU;

int main() {
	
	int tc;
	cin >> tc;
	cin.get();
	while (tc--) {
		VU v;
		string l, l2;
		
		cin.get();
		getline(cin, l);
		getline(cin, l2);
		stringstream iss(l), iss2(l2);
		unsigned i;
		while (iss >> i) {
			v.push_back(i);
		}
		string vs[v.size()];
		VU::iterator it = v.begin();
		while (iss2 >> l) {
			vs[(*it++)-1] = l;
		}
		for (i = 0; i < v.size(); i++)
			cout << vs[i] << endl;
		if (tc > 0)
			cout << endl;
	}
	
}
