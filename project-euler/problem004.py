#!/usr/bin/env python3

########################################################################
#   Solves problem 4 from projectEuler.net.
#   Finds the largest palindrome product of two 3-digt numbers.
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

from CommonFunctions import is_palindrome

if __name__ == '__main__':
    result = 0
    n1 = 100
    while n1 < 1000:
        n2 = n1
        while n2 < 1000:
            if is_palindrome(n1 * n2):
                result = max(result, (n1 * n2))
            n2 += 1
        n1 += 1
    print("The result is:", result)

