#include <iostream>
#include <string>
#include <map>
#include <stdio.h>

using namespace std;

int main(int argc, char** argv)
{
	map<string, double> conv;
    map<string, string> conv_str;
    int cases;
    double in, out;
    string unit;
    
    conv["kg"] = 0.4536;
    conv["lb"] = 2.2046;
    conv["l"] = 3.7854;
    conv["g"] = 0.2642;
    conv_str["kg"] = "lb";
    conv_str["lb"] = "kg";
    conv_str["l"] = "g";
    conv_str["g"] = "l";
    
    cin >> cases;
    for (int caso = 1; caso <= cases; caso++) {
        cin >> in;
        cin >> unit;
        cout << caso << " ";
        out = in * conv[conv_str[unit]];
        printf("%.4f %s\n", out, conv_str[unit].c_str());
    }
	return 0;
}
