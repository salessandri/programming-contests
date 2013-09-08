#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <string.h>
#include <cmath>

using namespace std;

typedef pair<long double, long double> PDD;
typedef pair<int, int> PII;
typedef pair<PDD, int> tower;
typedef vector<tower> VT;
typedef vector<PDD> VPDD;

inline long long rr(long double t) {
	if (t - (long long)t > 0.5)
		return (long long)t + 1;
	else
		return (long long)t;
}

char calculate_tower(const PDD &point,const VT &towers) {
	char res;
	long long max = -1;
	for (size_t i = 0; i < towers.size(); i++) {
		long double delta_x = towers[i].first.first - point.first;
		long double delta_y = towers[i].first.second - point.second;
		long long range = rr(towers[i].second / ((delta_x * delta_x) + (delta_y * delta_y)));
		if (range > max) {
			max = range;
			res = 'A' + i;
		}
	}
	return res;
}

int main() {
	int t, r;
	cin >> t;
	while (t) {
		cin >> r;
		VT towers;
		while (t--) {
			long double x, y;
			int p;
			cin >> x >> y >> p;
			towers.push_back(tower(PDD(x, y), p));
		}
		
		VPDD points;
		r++;
		while (r--) {
			long double x, y;
			cin >> x >> y;
			points.push_back(PDD(x, y));
		}
		long double resto = 0;
		long long pole = 0;
		char current = calculate_tower(points[0], towers);
		cout << "(" << pole << "," << current << ")";
		long double total = 0;
		for (unsigned i = 1; i < points.size(); i++) {
			long double x = points[i-1].first;
			long double y = points[i-1].second;
			long double delta_x = points[i].first - x;
			long double delta_y = points[i].second - y;
			long double d = sqrt(delta_x * delta_x + delta_y * delta_y);
			//long double d_mod = d - resto;
			//resto = d_mod - (int)d_mod;
			for (int j = 0; j < (int)d; j++) {
				pole++;
				x += (delta_x / d) * (1 - resto);
				y += (delta_y / d) * (1 - resto);
				char act = calculate_tower(PDD(x, y), towers);
				if (act != current) {
					cout << " (" << pole << "," << act << ")";
					current = act;
				}
				resto = 0;
			}
			total += d;
			resto = total - (int)total;
		}
		
		if (resto >= 0.5) {
			pole++;
			char act = calculate_tower(PDD(points.back().first, points.back().second), towers);
			if (act != current) {
				cout << " (" << pole << "," << act << ")";
				current = act;
			}
		}
			
		cout << endl;
		cin >> t;
	}
	
	return 0;
}
