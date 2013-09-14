#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

typedef pair<double, double> PDD;

/*
 * volume (x) = x * (y - 2x) * (z - 2x)
 * delta x = 12x^2 -x + zy
 * delta'' x = 24x -(4y-4z)
 */

PDD solutions(double y, double z) {
	double a = 12.0;
	double b = -4.0 * (y + z);
	double c = z * y;
	double first = min(y, z) * 0.5;
	double second = (-b - sqrt(b * b - 4.0 * a * c)) / (2.0 * a);
	return PDD(first, second);
	 
}

int main() {
	double y, z;
	
	while (cin >> y >> z) {
		PDD roots = solutions(y, z);
		printf("%.3f 0.000", roots.second);
		printf(" %.3f", roots.first);
		printf("\n");
	}
}
