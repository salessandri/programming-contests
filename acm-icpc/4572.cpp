#include <iostream>
#include <string>
#include <map>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;

struct Program{
	int mem;
	list<char> dlls;
	Program(int i) : mem(i) { }
};



unsigned nDlls, nProgs, nTrans;


inline unsigned abss(int x) {
	return (x < 0) ? -1 * x : x;
}

typedef map<char, int> MP;

int main() {
	cin >> nDlls;
	while(nDlls > 0) {
		
		MP dlls;
		vector<Program> programs;
		
		int buff;
		cin >> nProgs >> nTrans;
		vector<int> dllMem, programCount(nProgs, 0);
		for(unsigned i = 0; i < nDlls; i++) {
			cin >> buff;
			dllMem.push_back(buff);
			dlls[i + 'A'] = 0;
		}
		for(unsigned i = 0; i < nProgs; i++) {
			string line;
			cin >> buff;
			programs.push_back(buff);
			cin >>  line;
			for(unsigned index = 0; index < line.size(); index++) {
				programs.back().dlls.push_back(line[index]);
			}
		}
		int maxMem = 0, currentMem = 0;
		for(unsigned i = 0; i < nTrans; i++) {
			cin >> buff;
			if(buff > 0) {
				buff--;
				programCount[buff]++;
				currentMem += programs[buff].mem;
				for(list<char>::iterator it = programs[buff].dlls.begin(); it != programs[buff].dlls.end(); it++) {
					MP::iterator mapIt = dlls.find(*it);
					if(mapIt->second == 0) {
						currentMem += dllMem[*it - 'A'];
					}
					mapIt->second++;
				}
				maxMem = max(maxMem, currentMem);
			}
			else {
				buff = abss(buff) - 1;
				programCount[buff]--;
				currentMem -= programs[buff].mem;
				for(list<char>::iterator it = programs[buff].dlls.begin(); it != programs[buff].dlls.end(); it++) {
					MP::iterator mapIt = dlls.find(*it);
					if(mapIt->second == 1) {
						currentMem -= dllMem[*it - 'A'];
					}
					mapIt->second--;
				}
			}
		}
		cout << maxMem << endl;
		
		cin >> nDlls;
	}
}

