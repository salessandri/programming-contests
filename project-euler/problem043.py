#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 43 from projectEuler.net.
#   Finds the sum of all the numbers with a property.
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

from itertools import permutations

index = [0, 2, 3, 5, 7, 11, 13, 17]

def has_divisibility_property(n):
    str_n = str(n)
    for i in range(1,8):
        num = str_n[i:i+3]
        if int(num) % index[i] != 0:
            return False
    return True

if __name__ == '__main__':
    digits = set(str(x) for x in range(0, 10))
    result = 0
    for x in range(1,10):
        tmp = digits.copy()
        tmp.remove(str(x))
        result += sum(int(str(x) + ''.join(i)) for i in permutations(tmp) if
                      has_divisibility_property(str(x) + ''.join(i)))
    print("The result is:", result)
