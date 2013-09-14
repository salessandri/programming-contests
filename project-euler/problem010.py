#!/usr/bin/env python3

########################################################################
#   Solves problem 10 from projectEuler.net.
#   Finds the sum of the primes below 2 millon.
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
    result = 0
    lst = list(range(2, 2000000))
    for i in range(0, len(lst)):
        interval = lst[i]
        if (interval != -1):
            result += interval
            j = i + interval
            while j < len(lst):
                lst[j] = -1
                j += interval
    print("The result is:", result)

