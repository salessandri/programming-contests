#include <iostream>
#include <string>
#include <cctype>

using namespace std;

string decode_line(const string& encoded_line) {
    if (encoded_line.size() == 0) {
        return "";
    }
    if (encoded_line.size() == 1) {
        string decoded_line(encoded_line);
        if (isalpha(decoded_line[0])) {
            switch (decoded_line[0]) {
                case 'a':
                    decoded_line[0] = 'z';
                    break;
                case 'A':
                    decoded_line[0] = 'Z';
                    break;
                default:
                    decoded_line[0] -= 1;
            }
        }
        return decoded_line;
    }
    int left_size = (encoded_line.size()-1) / 2;
    int right_size = encoded_line.size() - 1 - left_size;
    string left_part = encoded_line.substr(1, left_size);
    string right_part = encoded_line.substr(1 + left_size, right_size);
    string middle_part = encoded_line.substr(0, 1);

    return decode_line(left_part) + decode_line(middle_part) + decode_line(right_part);
}

int main() {
    string encoded_line;
    while (getline(cin, encoded_line)) {
        cout << decode_line(encoded_line) << '\n';
    }

}