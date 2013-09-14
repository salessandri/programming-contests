#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 32 from projectEuler.net.
#   Finds the sum of all products whose multiplicand/multiplier/product
#   identity is pandigital.
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

from CommonFunctions import is_pandigital

if __name__ == '__main__':
    result = set()
    x = 2
    while len(str(x) * 2 + str(x ** 2)) <= 9:
        y = x + 1
        while len(str(x) + str(y) + str(x * y)) <= 9:
            if (x * y) not in result and is_pandigital(str(x) + str(y) + str(x * y)):
                result.add(x * y)
            y += 1
        x += 1
    result = sum(result)
    print("The result is:", result)