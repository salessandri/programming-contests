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
    

int main(int argc, char** argv)
{
	int cases;
    
    string line;
    
    cin >> cases;
    for (int caso = 1; caso <= cases; caso++) {
        memset(matrix, '0', 21*21*sizeof(char));
        cin >> rows >> columns;
        cin.get();
        getline(cin, line);
        
        
        
        dirs[0] = columns-1;
        dirs[1] = rows-1;
        dirs[2] = 0;
        dirs[3] = 1;
        int x, y;
        
        for (y = 0; y < rows; y++) {
            for (x = 0; x < columns; x++) {
                matrix[x][y] = line[y*columns + x];
            }
        }
        to_insert = "";
        x = y = 0;
        int dir = 0;
        for (size_t i = 0; i < line.size(); i++) {
            to_insert += matrix[x][y];
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
        string res = "";
        for (size_t i = 0; i < ((size_t)(to_insert.size() / 5)) * 5; i+= 5) {
            char c = 0;
            
            for (int j = 4; j >= 0; j--) {
                c = c | ((to_insert[i+4-j] - '0') << j);
            }
            
            if (c == 0)
                res += ' ';
            else
                res += (char)(c-1+'A');
        }
        while (*res.rbegin() == ' ') {
            res.erase(res.begin() + res.size() -1);
        }
        cout << res;
        cout << endl;
    }
	return 0;
}
