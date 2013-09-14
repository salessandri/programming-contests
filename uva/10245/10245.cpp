#include <iostream>
#include <utility>
#include <cmath>
#include <algorithm>
#include <cstdio>

using namespace std;

typedef pair<int, int> point;

bool myfunction_x (point i,point j) { return (i.first < j.first); }
bool myfunction_y (point i,point j) { return (i.second < j.second); }

long calc_min(point* arr_x, point* arr_y, int len, int len_y) {
    long diff_x, diff_y;
    if (len <= 3) {
        long min_dist = 999999999;
        diff_x = arr_x[0].first - arr_x[1].first;
        diff_y = arr_x[0].second - arr_x[1].second;
        for (int i = 0; i < len-1; i++) {
            for (int j = i+1; j < len; j++) {
                min_dist = min(min_dist, diff_x * diff_x + diff_y * diff_y);
            }
        }
        return min_dist;
    }
    int mx = arr_x[len/2].first;
    point arr_y_izq[10001], arr_y_der[10001];
    int len_y_izq = 0, len_y_der = 0;
    for (int i = 0; i < len; i++) {
        if (arr_y[i].first > mx)
            arr_y_der[len_y_der++] = arr_y[i];
        else {
            arr_y_izq[len_y_izq++] = arr_y[i];
        }
    }
    long dmin = min(calc_min(arr_x, arr_y_izq, len/2, len_y_izq),
                    calc_min(arr_x+(len/2), arr_y_der, len-(len/2), len_y_der));

    point arr_y_s[10001];
    int len_y_s = 0;
    for (int i = 0; i < len; i++) {
        long abs_dist = mx - arr_y[i].first;
        abs_dist = abs_dist < 0? abs_dist * - 1 : abs_dist;
        if (abs_dist < dmin)
            arr_y_s[len_y_s++] = arr_y[i];
    }
    for (int i = 0; i < len_y_s - 1; i++) {
        int k = i + 1;
        while ((k < len) && (arr_y_s[k].second - arr_y_s[i].second < dmin)) {
            diff_x = arr_y_s[k].first - arr_y_s[i].first;
            diff_y = arr_y_s[k].second - arr_y_s[i].second;
            dmin = min(dmin, diff_x * diff_x + diff_y * diff_y);
            k++;
        }
    }
    return dmin;
}

int main() {
    int n, i;
    int x, y;
    long minim,  limit = 10000 * 10000;
    point arr_x[10001], arr_y[10001];
    scanf("%d", &n);
    while (n) {
        minim = 999999999;
        for (i = 0; i < n; i++) {
            scanf("%d %d", &x, &y);
            arr_x[i].first = x;
            arr_x[i].second = y;
            arr_y[i].first = x;
            arr_y[i].second = y;
        }
        sort(arr_x, arr_x+n, myfunction_x);
        sort(arr_y, arr_y+n, myfunction_y);
        minim = calc_min(arr_x, arr_y, n, n);
        if (minim < limit) 
            printf("%.4lf\n", sqrt(minim));
        else
            printf("INFINITY\n");
        scanf("%d", &n);
    }
}
