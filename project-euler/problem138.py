#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 138 from projectEuler.net.
#   Finds the sum of the common side of the first twelve iscoseles
#   triangles with a property.
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
#   Visit my wiki at http://san-ss.wikidot.com
########################################################################

from itertools import islice

def get_triangle(m, n):
    a = m * n
    b = (n ** 2 - m ** 2) // 2
    c = (n ** 2 + m ** 2) // 2
    return (a, b, c)
    
def fib_generator():
    i1 = 1
    i2 = 1
    while True:
        for i in range(3):
            i1, i2 = (i2, i1 + i2)
        yield (i1, i2)

if __name__ == '__main__':
    result = 0
    for height, base, l in (get_triangle(n, m) for n, m in islice(fib_generator(), 12)):
        mult = 1
        while abs(((base * mult) * 2) - (height * mult)) != 1:
            mult += 1
        result += l * mult
    print("The result is:", result)