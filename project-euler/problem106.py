#!/usr/bin/env python3

########################################################################
#   Solves problem 106 from projectEuler.net.
#   Determines how many subset pairs that can be obtained need to be 
#   tested for equality with n = 12.
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

from itertools import zip_longest, combinations, product
from functools import reduce

def filt_func(c1, c2):
    if c1[0] > c2[0]:
        return False
    return not reduce(lambda x, y: x and (y[0] < y[1]), zip_longest(sorted(c1), sorted(c2)), True)

def generator(n, k):
    s1 = combinations(range(n), k // 2)
    comb_total = []
    for comb1 in s1:
        left_nums = set(range(n)) - set(comb1)
        s2 = (c for c in combinations(left_nums, k // 2) if filt_func(comb1, c))
        comb_total.extend(product([comb1], s2))
    return comb_total

if __name__ == '__main__':
    result = sum(len(generator(12, i)) for i in range(4, 13, 2))
    print("The result is:", result)
