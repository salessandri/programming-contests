#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 37 from projectEuler.net.
#   Finds the sum of the eleven truncable primes.
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
from itertools import islice, count

primes = set(find_primes_less_than(1000000))

def is_truncable(i):
    if i < 10:
        return False
    tmp = str(i)
    for x in range(len(tmp)):
        if (int(tmp[x:]) not in primes) or (int(tmp[:x + 1]) not in primes):
            return False
    return True

if __name__ == '__main__':
    result = sum(islice(filter(is_truncable, primes), 11))
    print("The result is:", result)
    