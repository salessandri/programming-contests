#include <iostream>

using namespace std;

int main() {
    char c, d;
    cout << "Ready" << endl;
    c = cin.get();
    d = cin.get();
    while ((c != ' ') && (d != ' ')) {
        if ((c == 'q') && (d == 'p'))
            cout << "Mirrored pair" << endl;
        else if ((c == 'p') && (d == 'q'))
            cout << "Mirrored pair" << endl;
        else if ((c == 'b') && (d == 'd'))
            cout << "Mirrored pair" << endl;
        else if ((c == 'd') && (d == 'b'))
            cout << "Mirrored pair" << endl;
        else
            cout << "Ordinary pair" << endl;
        cin.get();
        c = cin.get();
        d = cin.get();
    }
}
