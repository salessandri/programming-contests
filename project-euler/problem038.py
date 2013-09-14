#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 38 from projectEuler.net.
#   Finds largest 1-9 pandigital number formed by the concatenation of
#   a number with 1,2,..n.
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

from CommonFunctions import is_pandigital

if __name__ == '__main__':
    result = "0"
    for x in range(2,10000):
        tmp = str(x * 1) + str(x * 2)
        n = 3
        while len(tmp) < 9:
            tmp += str(x * n)
            n += 1
        if is_pandigital(tmp):
            result = max(int(result), int(tmp))
    print("The result is:", result)
