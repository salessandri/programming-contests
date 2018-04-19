#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

int main() {
	int n, s, t;
	cin >> n;
	while (n) {
		cin >> s >> t;
		int result[n+s][t];
		memset(result, 0, (n+s) * t * sizeof(int));
		for (int i = 0; i < n; i++)
			result[i][0] = -99999999;
		int board[n];
		for (int i = 0; i < n; i++)
			cin >> board[i];
		for (int row = n-1; row >= 0; row--) {
			for (int col = 1; col < t; col++) {
				result[row][col] = -99999999;
				for (int avance = 1; avance <= s; avance++) {
					result[row][col] = max(result[row][col], board[row] + result[row+avance][col-1]);
				}
			}
		}
		int def_result = result[0][t-1];
		for (int avance = 1; avance < s; avance++) {
			def_result = max(def_result, result[avance][t-1]);
		}
		cout << def_result << endl;
		cin >> n;
	}

}
