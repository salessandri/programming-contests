#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 49 from projectEuler.net.
#   Finds the a sequence of numbers with a property.
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
from itertools import dropwhile

is_anagram = lambda x, y: sorted(str(x)) == sorted(str(y))

if __name__ == '__main__':
    primes = find_primes_less_than(10000)
    primes_greater_1000 = dropwhile(lambda x: x <= 1000, primes)
    primes = set(primes)
    found_one = False
    for base in primes_greater_1000:
        for increment in range(1, ((10000 - base) // 2)):
            n1 = base + increment
            n2 = base + increment * 2
            if n1 in primes and n2 in primes and is_anagram(base, n1) and is_anagram(base, n2):
                if found_one:
                    print("The result is:", str(base) + str(n1) + str(n2))
                    exit(0)
                found_one = True
    