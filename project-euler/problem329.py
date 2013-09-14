#!/usr/bin/env python3

########################################################################
#   Solves problem 329 from projectEuler.net.
#   Calculates the probability of a series of croaks.
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

from CommonFunctions import find_primes_less_than
from fractions import Fraction

d = {}

primes = set(find_primes_less_than(501))
for i in range(1, 501):
    if i in primes:
        d[(i, 'P')] = Fraction(2, 3)
        d[(i, 'N')] = Fraction(1, 3)
    else:
        d[(i, 'P')] = Fraction(1, 3)
        d[(i, 'N')] = Fraction(2, 3)

def calc_prob(i, string):
    if (i, string) in d:
        return d[(i, string)]
    
    if (i == 1):
        prob = d[(i, string[0])] * calc_prob(i + 1, string[1:])
    elif (i == 500):
        prob = d[(i, string[0])] * calc_prob(i - 1, string[1:])
    else:
        prob = d[(i, string[0])] * (calc_prob(i + 1, string[1:]) * Fraction(1, 2) + calc_prob(i - 1, string[1:]) * Fraction(1, 2))
    
    d[(i, string)] = prob
    return prob

if __name__ == '__main__':
	result = Fraction(0, 1)
	for i in range(1, 501):
		result += calc_prob(i, 'PPPPNNPPPNPPNPN')
	print("The result is:", result / 500)
