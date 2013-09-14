#!/usr/bin/env python3

########################################################################
#   Solves problem 14 from projectEuler.net.
#   Finds the number below 1 million whose chain is the longest in
#   the 3n+1 sequence.
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

def len_seq(n):
    length = 1
    while n > 1:
        if n & 1 == 0:
            n = n >> 1
        else:
            n = 3 * n + 1
        length += 1
    return length

if __name__ == '__main__':
    maxN = 0
    lengthMax = 0
    for i in range(2, 1000000):
        lenN = len_seq(i)
        if lenN > lengthMax:
            maxN = i
            lengthMax = lenN
    print("The result is:", maxN)
