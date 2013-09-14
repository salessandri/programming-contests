#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 35 from projectEuler.net.
#   Finds the number of circular primes under 1000000.
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

from CommonFunctions import find_primes_less_than

primes = set(find_primes_less_than(1000000))

def is_circular_prime(n):
    for i in range(0, len(str(n)) + 1):
        n = int(str(n)[-1] + str(n)[:-1])
        if n not in primes:
            return False
    return True

if __name__ == '__main__':
    result = len([i for i in primes if is_circular_prime(i)])
    print("The result is:", result)
    