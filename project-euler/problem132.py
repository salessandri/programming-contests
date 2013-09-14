#!/usr/bin/env python3

########################################################################
#   Solves problem 132 from projectEuler.net.
#   Finds the first 40 prime factors of 10^(10^9) - 1.
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

if __name__ == '__main__':
    primes = find_primes_less_than(10 ** 6)
    base = 10
    exp = 10 ** 9
    result = sum(islice((p for p in primes if mod_pow(base, exp, 9 * p) == 1), 0, 40))
    print("The result is:", result)    
