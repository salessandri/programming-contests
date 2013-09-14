#!/usr/bin/python

########################################################################
#   Solves problem 166 from projectEuler.net.
#   Determines different 4x4 matrix that all columns, rows and diagonals
#   sum up the same.
#   Copyright (C) 2010  Santiago Alessandri
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#	
#   You can contact me at san.lt.ss@gmail.com 
#   Visit my wiki at http://san-ss.wikidot.com
########################################################################

mydict = {}

if __name__ == '__main__':
    for i in xrange(0, 10000):
        str_i = str(i)
        while (len(str_i) < 4):
            str_i = "0" + str_i
        suma = sum(map(int, str_i))
        mydict[suma] = mydict.get(suma, [])
        mydict[suma].append(str_i)
    
    result = 0
    
    for i in mydict.keys():
        print "Voy por el " + str(i)
        mydict[i].sort()
        for index1 in xrange(0, len(mydict[i])):
            n1 = mydict[i][index1]
            for index2 in xrange(index1, len(mydict[i])):
                n2 = mydict[i][index2]
                b = True
                for j in xrange(4):
                    if (int(n1[j]) + int(n2[j]) > i):
                        b = False
                        break
                if not b:
                    continue
                for index3 in xrange(index2, len(mydict[i])):
                    n3 = mydict[i][index3]
                    b = True
                    n4 = ''
                    for j in xrange(4):
                        if (int(n1[j]) + int(n2[j]) + int(n3[j]) > i):
                            b = False
                            break
                        else:
                            n4 += str(i - int(n1[j]) + int(n2[j]) + int(n3[j]))
                    if not b:
                        continue
                    if int(n1[0]) + int(n2[1]) + int(n3[2]) + int(n4[3]) != i:
                        continue
                    if int(n1[3]) + int(n2[2]) + int(n3[1]) + int(n4[0]) != i:
                        continue
                    if (n1 == n2) and (n1 == n3) and (n1 == n4):
                        result += 1
                    elif (n1 == n4):
                        result += 2
                    else:
                        result += 4
    
    print result
