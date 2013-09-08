#include <iostream>
#include <string>
#include <deque>
#include <sstream>
#include <cctype>
#include <cstdlib>


using namespace std;

inline string createString(char value) {
	ostringstream str;
	str << value;
	return str.str();
}

string process() {
	char value;
	deque<string> cola;
	cin >> value;
	while(value != '$') {
		switch(value) {
			case '(':
				cola.push_back(process());
				break;
			default:
				if(isdigit(value)) {
					string retValue;
					int n = value - 0x30;
					for(deque<string>::iterator it = cola.begin(); it < cola.end(); it++)
						retValue += *it;
					string retret;
					while(n--) {
						retret += retValue;
					}
					cin >> value;
					return retret;
				}
				else {
					cola.push_back(createString(value));
				}
				break;
		}
		cin >> value;
	}
	if(!cola.size())
		exit(0);
	string retValue;
	for(deque<string>::iterator it = cola.begin(); it < cola.end(); it++)
		retValue += *it;
	return retValue;
}



int main() {
	while(true)
		cout << process() << endl;
}



