#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 33 from projectEuler.net.
#   Finds the denominator of the product of 4 fractions with a property
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

from fractions import Fraction

def is_weird_fraction(num, denom):
    main = Fraction(num, denom)
    simplified = []
    if num % 10 == denom % 10:
        simplified.append(Fraction(num // 10, denom // 10))
    if num % 10 == denom // 10:
        simplified.append(Fraction(num // 10, denom % 10))
    if num // 10 == denom % 10:
        simplified.append(Fraction(num % 10, denom // 10))
    if num // 10 == denom // 10:
        simplified.append(Fraction(num % 10, denom % 10))
    for fract in simplified:
        if main == fract:
            return True
    return False

if __name__ == '__main__':
    lst = []
    for num in range(10, 100):
        for denom in range(num+1, 100):
            if not(num % 10 == 0 or denom % 10 == 0) and is_weird_fraction(num, denom):
                lst.append(Fraction(num, denom))
    result = Fraction(1,1)
    for f in lst:
        result *= f
    print("The result is:", result.denominator)