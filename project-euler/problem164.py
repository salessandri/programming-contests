#!/usr/bin/env python3

########################################################################
#   Solves problem 164 from projectEuler.net.
#   The number of 20 digit numbers such that no three consecutive digits
#   sum greater than 9.
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
#   Visit my wiki at http://san-ss.is-a-geek.com.ar
########################################################################

from itertools import product

d = {}

for i in range(0, 10):
    for j in range(0, 10):
        d[(1, i, j)] = 10 - i

def solve(*args):
    if args in d:
        return d[args]
    l, sum_last, last_dig = args
    result = 0
    for i in range(0, 10 - sum_last):
        result += solve(l - 1, last_dig + i, i)
    d[args] = result
    return result

if __name__ == '__main__':
    result = 0
    for t in filter(lambda x: x[0] < 10, 
                    map(lambda t: (sum(t), t[1]), 
                        product(range(1, 10), range(0, 10))
                        )
                    ):
        tmp = solve(18, *t)
        result += tmp
    print("The result is:", result)
