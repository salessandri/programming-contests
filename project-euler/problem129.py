#!/usr/bin/env python3

########################################################################
#   Solves problem 129 from projectEuler.net.
#   Finds the n so that the first R(k) divisible by n is > R(10 ** 6).
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
#   Visit my wiki at http://wiki.san-ss.com.ar
#   Visit my blog at http://blog.san-ss.com.ar
########################################################################

from CommonFunctions import *
from itertools import *

def A(n):
    i = 2
    while (mod_pow(10, i, 9 * n) != 1):
        i += 1
    return i

limit = 10 ** 6

if __name__ == '__main__':
    for n in count(1000001, 2):
        if str(n)[-1] == '5':
            continue
        x = A(n)
        if x > limit:
            break
    print("The result is:", n)
