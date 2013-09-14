#!/usr/bin/env python3

########################################################################
#   Solves problem 12 from projectEuler.net.
#   Finds the first triangular number with over 500 divisors.
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

from CommonFunctions import factors

if __name__ == '__main__':
    i = 5
    triangle = i * (i + 1) // 2
    divisors = factors(triangle)
    while len(divisors) <= 500:
        i += 1
        triangle = i * (i + 1) // 2
        divisors = factors(triangle)
    print("The result is:", triangle)