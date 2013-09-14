#include <iostream>
#include <cstring>
#include <algorithm>
#include <utility>

using namespace std;

typedef pair<int, int> PII;

enum FACE { FRONT, BACK, LEFT, RIGHT, TOP, BOTTOM, FACEEND };
const char *strings[] = { "front", "back", "left", "right", "top", "bottom" };

unsigned cubes[500][FACEEND];
int dp[500][101];

inline unsigned reverseFace(int aFace) {
	return (aFace & 1) ? aFace - 1 : aFace + 1;
}

bool backtrace(size_t color, size_t cube) {
    int size = dp[cube][color];
    size_t side = FRONT;
	while (cubes[cube][side] != color)
		side++;
	if (size > 1) {
		while(true) {
			int prev_cube = cube - 1;
			int bottom_color = cubes[cube][reverseFace(side)];
			while (prev_cube >= 0 && dp[prev_cube][bottom_color] != size -1)
				prev_cube--;
			if(prev_cube < 0 || !backtrace(bottom_color, prev_cube)) {
				side++;
				while (side < FACEEND && cubes[cube][side] != color)
					side++;
				if(side >= FACEEND)
					return false;
				continue;
			}
			break;
		}
	}
	cout << cube + 1 << " " << strings[reverseFace(side)] << endl;
    return true;
} 

int main() {
	int currentCase(1);
    int nCubes;
	cin >> nCubes;
    while(nCubes > 0) {
        if (currentCase > 1)
            cout << endl;
        int max_max = -1;
        int max_color = 0;
		memset(cubes, 0, 500 * FACEEND * sizeof(unsigned));
        memset(dp, 0, 500 * 101 * sizeof(int));
        PII maximum[101];
        for (int i = 0; i < 101; i++) {
            maximum[i].first = 0;
        }
		for(int i = 0; i < nCubes; i++) {
			for(int j = 0; j < FACEEND; j++) {
				cin >> cubes[i][j];
			}
            for (int j = 0; j < FACEEND; j++) {
                int reverse_face_color = cubes[i][reverseFace(j)];
                dp[i][cubes[i][j]] = max(dp[i][cubes[i][j]], maximum[reverse_face_color].first + 1);
            }
            for (int j = 0; j < FACEEND; j++) {
                if (dp[i][cubes[i][j]] > maximum[cubes[i][j]].first) {
                    maximum[cubes[i][j]].first = dp[i][cubes[i][j]];
                    maximum[cubes[i][j]].second = i;
                    if (maximum[cubes[i][j]].first > max_max) {
                        max_max = maximum[cubes[i][j]].first;
                        max_color = cubes[i][j];
                    }
                }
            }
		}
        cout << "Case #" << currentCase++ << endl;
        cout << max_max << endl;
        backtrace(max_color, maximum[max_color].second);
        cin >> nCubes;
    }
}
