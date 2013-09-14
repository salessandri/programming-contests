#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 41 from projectEuler.net.
#   Finds the largest n-pandigital prime.
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

from CommonFunctions import is_prime
from itertools import permutations

if __name__ == '__main__':
    result = 0
    for i in range(3,10):
        for x in permutations([str(x) for x in range(1,i+1)]):
            x = int(''.join(x))
            if is_prime(x):
                result = max(result, x)
    print("The result is:", result)