#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

struct flight {
    unsigned long start_time;
    unsigned long duration;
    unsigned long price;
    
    bool operator<(const flight& other) const {
        return !(start_time < other.start_time);
    }
};

void solve_case() {
    int n;
    cin >> n;
    vector<flight> flights(n);
    for (int i = 0; i < n; ++i) {
        cin >> flights[i].start_time >> flights[i].duration >> flights[i].price;
    }
    sort(flights.begin(), flights.end());
    
    map<unsigned long, unsigned long> time_profit;
    time_profit[10000000] = 0;
    for (vector<flight>::const_iterator it = flights.begin(); it != flights.end(); it++) {
        unsigned long current_best_from_now = time_profit.lower_bound(it->start_time)->second;
        unsigned long best_after_this_flight = time_profit.lower_bound(it->start_time + it->duration)->second;
        time_profit[it->start_time] = max(current_best_from_now, it->price + best_after_this_flight);
    }
      
    cout << time_profit.begin()->second << '\n';
}

int main() {
    int tests;
    cin >> tests;
    for (int i = 0; i < tests; ++i) {
        solve_case();
    }
}