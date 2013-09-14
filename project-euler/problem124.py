#!/usr/bin/env python3

########################################################################
#   Solves problem 124 from projectEuler.net.
#   Finds the n of the 10000th rad(n) of the first 100000 rads.
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

from CommonFunctions import find_primes_less_than

LIMIT = 100000

if __name__ == '__main__':
    primes = find_primes_less_than(LIMIT)

    rads = [[1, i] for i in range(LIMIT+1)]
    for p in primes:
        for i in range(p, LIMIT+1, p):
            rads[i][0] *= p
    print("The result is:", sorted(rads)[10000][1])
