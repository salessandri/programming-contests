#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>

using namespace std;

long long amount[] = {0, 1, 20, 300, 4000, 50000, 600000, 70000000, 800000000};
long long c_amount[] = {0, 0, 10, 90, 1010, 11110, 111110, 1111110, 11111110};

void calc(string a, unsigned long long *vec) {

        char c = a[0];
        int limit = c - '0';
        
        if (a.size() == 1) {
                for (int i = 0; i <= limit; i++)
                        vec[i]++;
                return;
        }

        for (int i = 1; i < limit; i++) {
                vec[i] += pow(10, a.size() - 1);
        }
        for (int i = 0; i < limit; i++) {
                for (int j = 0; j < 10; j++)
                        vec[j] += amount[a.size()-1];
        }
        if (c == '0')
			vec[0] -= pow(10, a.size() - 1);
        a.erase(a.begin());
        istringstream to_num(a);
        long long x;
        to_num >> x;
        vec[limit] += x + 1;
        calc(a, vec);
}

int main() {
        
        long long a, b;
		cin >> a >> b;
        while (a != 0) {
                unsigned long long vec_a[10];
                unsigned long long vec_b[10];
                memset(vec_a, 0, sizeof(long long) * 10);
                memset(vec_b, 0, sizeof(long long) * 10);
                ostringstream str_a, str_b;
                str_a << a - 1;
                str_b << b;
                calc(str_b.str(), vec_b);
                calc(str_a.str(), vec_a);
                
                for (unsigned i = 0; i < 9; i++)
                      cout << vec_b[i] - vec_a[i] << ' ';
                cout << vec_b[9] - vec_a[9] << endl;
                cin >> a >> b;
        }
        
}
