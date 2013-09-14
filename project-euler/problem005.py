#!/usr/bin/env python3

########################################################################
#   Solves problem 5 from projectEuler.net.
#   Finds the least common multiple of the first 20 integers.
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

if __name__ == '__main__':
    n = 20
    lt = list(range(1, n+1))
    for i in range(1, n):
        x = lt[i]
        index = i + 1
        while index < n:
            if (lt[index] % x) == 0:
                lt[index] //= x
            index += 1
    result = 1
    for elem in lt:
        result *= elem
    print("The result is:", result)