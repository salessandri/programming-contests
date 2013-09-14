#!/usr/bin/env python3

########################################################################
#   Solves problem 27 from projectEuler.net.
#   Finds the 2 coeficients of a quadratic function that generates the
#   longest sequence of primes and return the product.
#   Copyright (C) 2010  Santiago Alessandri
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

from CommonFunctions import find_primes_less_than, is_prime

if __name__ == '__main__':
    max = 0
    primes = find_primes_less_than(1000)
    for b in primes:
        for a in range(-999, 1000):
            n = 0
            tmp = n ** 2 + a * n + b
            while tmp > 0 and is_prime(tmp):
                n += 1
                tmp = n ** 2 + a * n + b
            if n > max:
                max = n
                res = (a, b)
    print("The result is:", res[0] * res[1])

