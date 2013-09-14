#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 46 from projectEuler.net.
#   Finds the first composite number that can't be expressed as the
#   sum between a prime and twice a square.
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

def has_property(n):
    index = 0
    while index < len(lst_two_squares) and lst_two_squares[index] < n:
        if (n - lst_two_squares[index]) in primes:
            return True
        index += 1
    return False

primes = set(find_primes_less_than(30000))
lst_two_squares = [2 * (i ** 2) for i in range(1,2000)]

if __name__ == '__main__':
    result = 9
    while has_property(result):
        result += 2
        while result in primes:
            result += 2
    print("The result is:", result)
