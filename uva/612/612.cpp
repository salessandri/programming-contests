#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

using namespace std;

typedef pair<int, string> PIS;
typedef vector<PIS> VPIS;

bool my_comp(PIS a, PIS b) {
	return a.first < b.first;
}

int main(){
	int tc;
	cin >> tc;
	while (tc--) {
		int l, cant;
		cin >> l >> cant;
		VPIS arr;
		while(cant--) {
			string str = "";
			int a = 0;
			int c = 0;
			int g = 0;
			int t = 0;
			int res = 0;
			cin.get();
			for (int i = 0; i < l; i++) {
				char ch = cin.get();
				switch (ch) {
					case 'T':
						res += g;
					case 'G':
						res += c;
					case 'C':
						res += a;
				}
				switch (ch) {
					case 'T':
						t++;
						break;
					case 'G':
						g++;
						break;
					case 'C':
						c++;
						break;
					case 'A':
						a++;
				}
				str += ch;
			}
			cin.get();
			arr.push_back(PIS(res, str));
		}
		sort(arr.begin(), arr.end(), my_comp);
		for (unsigned i = 0; i < arr.size(); i++)
			cout << arr[i].second << endl;;
		
		if (tc > 0)
			cout << endl;
	}
}
