#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    int index, value;
    Item() { }
    Item(int i, int v) : index(i), value(v) { }
};

static vector<Item> intersections[500001];
static int n;
int maxi;

int maxFor(int i) {
    int localMax1 = 0, localMax2 = 0, tmp, *unMax;
    if(!intersections[i].size())
        return 0;
    for(int x = 0; x < intersections[i].size(); x++) {
        tmp = maxFor(intersections[i][x].index) + intersections[i][x].value;
        unMax = (localMax1 < localMax2) ? &localMax1 : &localMax2;
        if(tmp > *unMax)
            *unMax = tmp;
    }
    if(localMax1 + localMax2 > maxi)
        maxi = localMax1 + localMax2;
    return ::max(localMax1, localMax2);
}

void cleanUp() {
    for(int i = 0; i < n; i++)
        intersections[i].clear();
}

int main() {
    cin >> n;
    while(n) {
        int i1, i2, value;
        for(i1 = 1; i1 < n; i1++) {
            cin >> i2 >> value;
            intersections[i2].push_back(Item(i1, value));
        }
        maxi = 0;
        maxFor(0);
        cout << maxi << endl;
        cin >> n;
        if(n)
            cleanUp();//plx
    }
}
