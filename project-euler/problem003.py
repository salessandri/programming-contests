#!/usr/bin/env python3

########################################################################
#   Solves problem 3 from projectEuler.net.
#   Finds the largest prime factor of 600851475143.
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

from CommonFunctions import is_prime

if __name__ == '__main__':
    i = 3
    number = 600851475143
    while number > 1:
        if is_prime(i):
            while (number % i) == 0:
                number //= i
        i += 2
    i -= 2
    print("The result is:", i)

