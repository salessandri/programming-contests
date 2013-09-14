#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 121 from projectEuler.net.
#   Finds the maximum prize fund taht should be allocated for a
#   special game.
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
from itertools import combinations, chain
from functools import reduce

turns = 15

if __name__ == '__main__':
    result = 0
    prob = [Fraction(1, x) for x in range(2, 2 + turns)]
    for cant in range(len(prob) // 2 + 1, len(prob) + 1):
        for comb in combinations(prob, cant):
            probabilites_per_turn = chain((Fraction(n-1, n) for n in range(2, 2+turns) if Fraction(1, n) not in comb), comb)
            result += reduce(lambda x,y: x*y, probabilites_per_turn)
    print("The result is:", result.denominator // result.numerator)

