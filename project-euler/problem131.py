#!/usr/bin/env python3

########################################################################
#   Solves problem 131 from projectEuler.net.
#   Finds the number of primes below 1 millon for which exists an n that
#   n ** 3 + (n ** 2) * p is a perfect cube.
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

from CommonFunctions import find_primes_less_than
from itertools import count, takewhile

primes = find_primes_less_than(int(1000000 ** 0.5))

def is_prime(n):
    limit = n ** 0.5
    for p in primes:
        if p > limit:
            return True
        if n % p == 0:
            return False
    return True

if __name__ == '__main__':
    result = sum(1 for i in 
                    takewhile(
                        lambda x: x < 1000000, 
                        ((i + 1) ** 3 - i ** 3 for i in count(1))
                    )
                    if is_prime(i)
                )
    print("The result is:", result)
