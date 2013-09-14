#!/usr/bin/env python3

########################################################################
#   Solves problem 57 from projectEuler.net.
#   Determines how many of the first 1000 expansions of the continued
#   fraction to solve sqrt(2) have the numerator longer than the 
#   denominator.
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
#   You can contact me at san.lt.ss@gmail.com or salessandri@nasel.com
#   Visit my wiki at http://san-ss.wikidot.com
########################################################################

from fractions import Fraction
from itertools import islice

def sqrt_2_continued_fraction():
    tmp = 2 + Fraction(1, 2)
    yield tmp
    while True:
        tmp = 2 + 1 / tmp
        result = 1 + 1 / tmp
        yield result

if __name__ == '__main__':
    result = sum(1 for frac in islice(sqrt_2_continued_fraction(), 1000) if
                 len(str(frac.numerator)) > len(str(frac.denominator)))
    print("The result is:", result)
