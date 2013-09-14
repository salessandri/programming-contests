#!/usr/bin/env python3

########################################################################
#   Solves problem 30 from projectEuler.net.
#   Finds all the integers that can be written as the sum of fifth
#   power of their digits.
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

def sum_of_digits_to(i, n):
    return sum(int(c) ** n for c in str(i))

if __name__ == '__main__':
    n = 5
    limit = '9'
    while (9 ** n) * len(limit) > int(limit):
        limit += '9'
    limit = int(limit)
    result = 0
    for i in range(10, limit+1):
        if sum_of_digits_to(i, n) == i:
            result += i
    print("The result is:", result)
