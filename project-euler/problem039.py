#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 39 from projectEuler.net.
#   Finds the perimeter below than 1000 that can be formed by the most
#   number of rectangular triangles of integral lengths.
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


def find_combinations_of_perimeter(per):
    result = 0
    a = 1
    b = 1
    c = 1
    for a in range(1, per // 2):
        for b in range(a, per // 2):
            c = per - b - a
            if (a ** 2 + b ** 2) == c ** 2:
                result += 1
    return result

if __name__ == '__main__':
    max_count = 0
    for i in range(12, 1000):
        c = find_combinations_of_perimeter(i)
        if c > max_count:
            max_count = c
            result = i
    print("The result is:", result)