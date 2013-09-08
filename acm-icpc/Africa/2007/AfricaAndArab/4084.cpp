#include <iostream>

using namespace std;

int main() {
	
	int n;
	cin >> n;
	while (true) {
		int sum = n;
		int mini = n;
		int maxi = n;
		for (int i = 0; i < 5; i++) {
			cin >> n;
			sum += n;
			if (n < mini)
				mini = n;
			if (n > maxi)
				maxi = n;
		}
		if ((mini == maxi) && (maxi == 0))
			break;
		sum -= (mini + maxi);
		float avg = sum / 4.0;
		if (avg == (int)avg)
			cout << (int)avg;
		else
			cout << avg;
		cout << endl;
		cin >> n;
	}
	return 0;
}
