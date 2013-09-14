#!/usr/bin/env python3

########################################################################
#   Solves problem 58 from projectEuler.net.
#   Determines what is the side length of the square spiral for which 
#   the ratio of primes along both diagonals first falls below 10%
#   fraction to solve sqrt(2) have the numerator longer than the 
#   denominator.
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

from CommonFunctions import is_prime
from itertools import takewhile

def sqr_diag_generator():
    cant_tot = 1
    cant_primes = 0
    num = 1
    to_sum = 2
    while True:
        for i in range(0,4):
            num += to_sum
            if is_prime(num):
                cant_primes += 1
        to_sum += 2
        cant_tot += 4
        
        yield cant_primes * 100 / cant_tot 
            
if __name__ == '__main__':
    result = 3 + sum(2 for i in takewhile(lambda p: p >= 10, sqr_diag_generator()))
    print("The result is:", result)
