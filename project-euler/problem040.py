#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 40 from projectEuler.net.
#   Finds the product of several digits in an irrational decimal fraction
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

from functools import reduce

if __name__ == '__main__':
    decimal_part = []
    i = 1
    while len(decimal_part) < 1000000:
        decimal_part.append(str(i))
        i += 1
    decimal_part = ''.join(decimal_part)
    result = reduce(lambda x, y: x * int(decimal_part[int('9' * y)]), range(1, 6), int(decimal_part[0]))
    print("The result is:", result)
