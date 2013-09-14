#!/usr/bin/env python3

########################################################################
#   Solves problem 151 from projectEuler.net.
#   Finds the expected number of times of a condition to happen
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

from decimal import *

d = {
    (5,) : Decimal(0)
}

def solve(curr_size):
    if curr_size in d:
        return d[curr_size]
    
    result = Decimal(0)
    
    if len(curr_size) == 1:
        result += Decimal(1)
    
    p = Decimal(1) / Decimal(len(curr_size))
    for i in curr_size:
        tmp_curr = list(curr_size)
        tmp_curr.remove(i)
        while (i < 5):
            tmp_curr.append(i + 1)
            i += 1
        tmp_curr = tuple(sorted(tmp_curr))
        result += p * solve(tmp_curr)
    
    d[curr_size] = result
    return result

if __name__ == '__main__':
    result = solve((2,3,4,5))
    getcontext().prec = 6
    result = +result
    print("The result is:", result)
