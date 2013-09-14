#!/usr/bin/env python3

########################################################################
#   Solves problem 75 from projectEuler.net.
#   Finds the number of different perimiters less than 1500000 that
#   can just form one interger sided right triangle.
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

from itertools import takewhile, count
from fractions import gcd

LIMIT = 1500000

if __name__ == '__main__':
    found_per = set()
    rep_per = set()
    generator = ((n, m) for n in count(3, 2) for m in range(1, n, 2) if gcd(m,n) == 1)
    for n, m in generator:
        a = m * n
        b = (n ** 2 - m ** 2) // 2
        c = (n ** 2 + m ** 2) // 2
        perimeter = a + b + c
        if m == 1 and perimeter > LIMIT:
            break
        
        for per in takewhile(lambda x: x <= LIMIT, (perimeter * i for i in count(1))):
            if per in found_per:
                rep_per.add(per)
            else:
                found_per.add(per)
    
    print("The result is", len(found_per - rep_per))
    
