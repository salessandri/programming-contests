#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

enum side {AB=0, AC, AD, BC, BD, CD};

int main() {
    int tc, sides[6];;
    cin >> tc;
    while (tc--){
        for (int i = AB; i <= CD; i++)
            cin >> sides[i];
        long double u_ = pow(sides[BC], 2) + pow(sides[BD], 2) - pow(sides[CD], 2);
        long double v_ = pow(sides[BD], 2) + pow(sides[AB], 2) - pow(sides[AD], 2);
        long double w_ = pow(sides[AB], 2) + pow(sides[BC], 2) - pow(sides[AC], 2);
        long double volume = sqrt(4 * pow(sides[AB],2) * pow(sides[BC],2) * pow(sides[BD],2) - pow(sides[AB], 2) * pow(u_, 2) - pow(sides[BC], 2) * pow(v_, 2) - pow(sides[BD], 2) * pow(w_, 2) + u_ * v_ * w_) / 12;
        printf("%.4Lf\n", volume);
    }
}
