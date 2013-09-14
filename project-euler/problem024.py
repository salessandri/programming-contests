#!/usr/bin/env python3

########################################################################
#   Solves problem 24 from projectEuler.net.
#   Finds the 1000000th lexicographic permutation of the 10 digits.
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

from CommonFunctions import factorial

def combinations(n, r):
    return factorial(n) // (factorial(n - r))

if __name__ == '__main__':
    number = 999999
    lst = list(range(10))
    result = []
    for i in range(9, -1, -1):
        comb = combinations(i, i)
        index = number // comb
        number = number % comb
        result.append(str(lst.pop(index)))
    print("The result is:", ''.join(result))
    

