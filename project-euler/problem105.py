#!/usr/bin/python3

########################################################################
#   Solves problem 105 from projectEuler.net.
#   Retrieves the sum of the sets which have 2 properties.
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

from itertools import combinations, product, zip_longest
from functools import reduce
from math import ceil

d = {}

def filt_func(c1, c2):
    if c1[0] > c2[0]:
        return False
    return not reduce(lambda x, y: x and (y[0] < y[1]), zip_longest(sorted(c1), sorted(c2)), True)

def generator(n, k):
    if (n, k) in d:
        return d[(n, k)]
    s1 = combinations(range(n), k // 2)
    comb_total = []
    for comb1 in s1:
        left_nums = set(range(n)) - set(comb1)
        s2 = (c for c in combinations(left_nums, k // 2) if filt_func(comb1, c))
        comb_total.extend(product([comb1], s2))
    d[(n, k)] = comb_total
    return comb_total

def check_cond1(s):
    for i in range(4, len(s) + 1, 2):
        for c1, c2 in generator(len(s), i):
            if sum(map(lambda x: s[x], c1)) == sum(map(lambda x: s[x], c2)):
                return False
    return True

def check_cond2(s):
    for i in range(2, ceil(len(s) / 2) + 1):
        if sum(s[:i]) <= sum(s[-(i - 1):]):
            return False
    return True

if __name__ == '__main__':
    sets = []
    for l in open('sets.txt'):
        s = sorted(map(int, l.strip().split(',')))
        sets.append(s)
    result = sum(sum(s) for s in sets if check_cond2(s) and check_cond1(s))
    print("The result is:", result)
