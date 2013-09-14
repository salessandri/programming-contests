#!/usr/bin/env python3

########################################################################
#   Solves problem 207 from projectEuler.net.
#   Finds the smallest M for which P(m) < 1/12345
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

from fractions import Fraction
from math import log

calc_k = lambda x: x * (x - 1)

cant_perf = 1
cant_tot = 1
limit = Fraction(1, 12345)

if __name__ == '__main__':
    i = 3
    while Fraction(cant_perf, cant_tot) >= limit:
        log_2 = int(log(i,2))
        if 2 ** log_2 == i:
            cant_perf += 1
        cant_tot += 1
        i += 1
    i -= 1
    print("The result is:", calc_k(i))

