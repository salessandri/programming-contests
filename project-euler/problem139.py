#!/usr/bin/env python3

########################################################################
#   Solves problem 139 from projectEuler.net.
#   Finds the number of integral right-angle triangles whose perimeter
#   is less than 100000000 and have a property.
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

LIMIT = 100000000

if __name__ == '__main__':
    result = 0
    generator = ((n, m) for n in count(3, 2) for m in range(1, n, 2) if gcd(m,n) == 1)
    for n, m in generator:
        a = m * n
        b = (n ** 2 - m ** 2) // 2
        c = (n ** 2 + m ** 2) // 2
        perimeter = a + b + c
        if perimeter > LIMIT and m == 1:
            break
        
        if c % (b - a) == 0:
            result += LIMIT // (a + b + c)
    print("The result is", result)
