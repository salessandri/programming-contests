#!/usr/bin/python3

########################################################################
#   Solves problem 183 from projectEuler.net.
#   Calculates the sum of the results of a special function from 5 to
#   10000.
#   Copyright (C) 2011  Santiago Alessandri
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

from math import ceil, e, floor
from fractions import gcd

if __name__ == '__main__':
    result = 0
    print(e)
    for n in range(5, 10001):
        
        denom = round(n / e)
        n_2 = n
        d = gcd(n_2, denom)
        while d > 1:
            n_2 /= d
            denom /= d
            d = gcd(n_2, denom)
        while denom % 2 == 0:
            denom /= 2
        while denom % 5 == 0:
            denom /= 5
        if denom == 1:
            result -= n
        else:
            result += n
    print("The result is:", result)
