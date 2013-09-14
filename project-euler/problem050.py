#!/usr/bin/env python3

########################################################################
#   Solves problem 50 from projectEuler.net.
#   Finds the prime below one millon which can be written as the sum of
#   most consecutive primes.
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

from CommonFunctions import find_primes_less_than
from itertools import takewhile

if __name__ == '__main__':
    primes = find_primes_less_than(1000000)
    prime_set = set(primes)
    max_len = 0
    result = 0
    for i in takewhile(lambda i: primes[i] <= 5000000,
                       range(len(primes))):
        tmp = primes[i]
        for j in takewhile(lambda j: tmp + primes[j] <= 1000000,
                           range(i + 1, len(primes))):
            tmp += primes[j]
            if j - i + 1 > max_len and tmp in prime_set:
                result = tmp
                max_len = j - i + 1
    print("The result is:", result)