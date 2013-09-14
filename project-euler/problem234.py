#!/usr/bin/env python3

########################################################################
#   Solves problem 234 from projectEuler.net.
#   Finds the sum of the semidivisible numbers below 999966663333
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

from itertools import takewhile, count
from CommonFunctions import find_primes_less_than

LIMIT = 999966663333

if __name__ == '__main__':
	primes = find_primes_less_than(1100000)
	result = 0

	for i in takewhile(lambda x: primes[x] ** 2 < LIMIT, count(0)):
		lower_bound = primes[i]
		lower_bound_2 = lower_bound ** 2
		upper_bound = primes[i + 1]
		upper_bound_2 = upper_bound ** 2
		set_mult_lower = set(range(lower_bound_2 + lower_bound, min(upper_bound_2 + 1, LIMIT + 1), lower_bound))
		set_mult_upper = set(range(min(upper_bound_2 - upper_bound, LIMIT - (LIMIT % upper_bound)), lower_bound_2 - 1, -upper_bound))
		result += sum((set_mult_lower | set_mult_upper) - (set_mult_lower & set_mult_upper))

	print("The result is:", result)
