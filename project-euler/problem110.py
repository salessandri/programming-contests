#!/usr/bin/env python3

########################################################################
#   Solves problem 110 from projectEuler.net.
#   Finds least value of n for which the number of distinct solutions 
#   exceeds four million in 1/x + 1/y = 1/n.
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
########################################################################

from functools import reduce
from CommonFunctions import find_primes_less_than

primes = find_primes_less_than(50)

mult = lambda x: reduce(lambda y, z: y * z, x, 1)

translate = lambda x: mult(primes[i] ** ((x[i] - 1) // 2) for i in range(len(x)))

def generator(limit):
    l = [1] * 14
    while l[13] < limit:
        i = 13
        while i > 0 and (l[i] == l[i-1]):
            l[i] = 1
            i -= 1
        l[i] += 2
        yield l

if __name__ == '__main__':
    result = min(translate(l) for l in generator(13) if mult(l) > 8000000)
    print("The result is:", result)
