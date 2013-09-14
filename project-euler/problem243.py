#!/usr/bin/env python3

########################################################################
#   Solves problem 234 from projectEuler.net.
#   Finds the sum of the semidivisible numbers below 999966663333
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

from fractions import Fraction
from itertools import takewhile

from CommonFunctions import find_primes_less_than, gcd, phi

primes = find_primes_less_than(10000)

def resilience(x):
    return Fraction(phi(x), (x-1))

limit = Fraction(15499, 94744)

if __name__ == '__main__':
    found = False
    mult_primes = primes[0]
    while not found:
        for i in range(1, primes[0] + 1):
            if (resilience(mult_primes * i) < limit):
                found = True
                break
        if not found:
            primes.pop(0)
            mult_primes *= primes[0]

print(mult_primes * i)
