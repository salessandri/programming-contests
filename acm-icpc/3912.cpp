#include <iostream>
#include <string>
#include <map>
#include <stdio.h>
#include <string.h>

using namespace std;

static char matrix[21][21];
int rows, columns;
int dirs[4];
string to_insert;

void to_bin(char c) {
    char index = 16;
    c = c == ' '?0: c-'A'+1;
    
    while (index) {
        to_insert += (c & index)? "1": "0";
        index >>= 1;
    }
    
}
    

int main(int argc, char** argv)
{
	int cases;
    
    string line;
    
    cin >> cases;
    for (int caso = 1; caso <= cases; caso++) {
        memset(matrix, '0', 21*21*sizeof(char));
        to_insert = "";
        cin >> rows >> columns;
        cin.get();
        getline(cin, line);
        dirs[0] = columns-1;
        dirs[1] = rows-1;
        dirs[2] = 0;
        dirs[3] = 1;
        for (size_t i = 0; i < line.size();  i++) {
            to_bin(line[i]);
        }
        int x, y;
        x = y = 0;
        int dir = 0;
        for (size_t i = 0; i < to_insert.size(); i++) {
            matrix[x][y] = to_insert[i];
            switch (dir) {
                case 0:
                    if (x < dirs[dir]) {
                        x++;
                    }
                    else {
                        dir = 1;
                        y++;
                        dirs[0]--;
                    }
                    break;
                case 1:
                    if (y < dirs[dir]) {
                        y++;
                    }
                    else {
                        dir = 2;
                        x--;
                        dirs[1]--;
                    }
                    break;
                case 2:
                    if (x > dirs[dir]) {
                        x--;
                    }
                    else {
                        dir = 3;
                        y--;
                        dirs[2]++;
                    }
                    break;
                case 3:
                    if (y > dirs[dir]) {
                        y--;
                    }
                    else {
                        dir = 0;
                        x++;
                        dirs[3]++;
                    }
                    break;
            }
        }
        cout << caso << " ";
        for (y = 0; y < rows; y++) {
            for (x = 0; x < columns; x++) {
                cout << matrix[x][y];
            }
        }
        cout << endl;
    }
	return 0;
}
