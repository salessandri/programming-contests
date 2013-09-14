#!/usr/bin/python3

########################################################################
#   Solves Google CodeJam 2009 Qualification Round's problem A
#   Copyright (C) 2011  Santiago Alessandri
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
#   Visit my wiki at http://wiki.san-ss.com.ar
#   Visit my blog at http://blog.san-ss.com.ar
########################################################################

words = set()

if __name__ == '__main__':
    L, D, N = map(int, input().split())
    for i in range(D):
        words.add(input())
    for i in range(1, N+1):
        characters = input()
        characters_set = []
        s = set()
        flag = True
        for c in characters:
            if c == '(':
                flag = False
            elif c == ')':
                flag = True
            else:
                s.add(c)
            if flag:
                characters_set.append(s)
                s = set()
        result = 0
        for word in words:
            t = True
            for k in range(L):
                if word[k] not in characters_set[k]:
                    t = False
                    break
            if t:
                result += 1
        print("Case #{0}: {1}".format(i, result))
