#include <iostream>
#include <cctype>

using namespace std;

int main() {
    string identifier;
    while (cin >> identifier) {
        bool ok = true;
        size_t i = 0;
        int type = 0;
        string new_identifier = "";
        while (i < identifier.size()) {
            if ((i == 0) && ((isupper(identifier[i])) || identifier[i] == '_')) {
                ok = false;
                break;
            }
            if ((type == 1) && (isupper(identifier[i]))) {
                ok = false;
                break;
            }
            if ((type == 2) && (identifier[i] == '_')) {
                ok = false;
                break;
            }
            if ((identifier[i] == '_') && ((i == identifier.size()-1) || (identifier[i+1] == '_') || isupper(identifier[i+1]))) {
                ok = false;
                break;
            }
            if (islower(identifier[i])) {
                new_identifier.push_back(identifier[i]);
                i++;
            }
            else if (isupper(identifier[i])) {
                new_identifier.push_back('_');
                new_identifier.push_back(tolower(identifier[i++]));
                type = 2;
            }
            else if (identifier[i] == '_') {
                i++;
                new_identifier.push_back(toupper(identifier[i++]));
                type = 1;
            }
        }
        if (ok)
            cout << new_identifier << endl;
        else
            cout << "Error!" << endl;

    }
}
