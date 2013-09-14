#!/usr/bin/env python3

########################################################################
#   Solves problem 52 from projectEuler.net.
#   Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and
#   6x, contain the same digits.
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

from itertools import takewhile, count

if __name__ == '__main__':
    mult = 1
    for result in takewhile(lambda x: mult < 6, count(1)):
        orig_set = set(str(result))
        tmp_set = set(str(result*2))
        mult = 2
        while orig_set == tmp_set:
            mult += 1
            tmp_set = set(str(result*mult))
    print("The result is:", result)