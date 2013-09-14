#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 47 from projectEuler.net.
#   Finds the first 4 integeres which have 4 distinct prime factors.
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

from CommonFunctions import find_primes_less_than

def find_prime_factors(n, primes):
    factores = set()
    index = 0
    while n > 1:
        if n % primes[index] == 0:
            i = 0
            while n % primes[index] == 0:
                n /= primes[index]
                i += 1
            factores.add("%d^%d" % (primes[index], i))
        else:
            index += 1
    return factores

if __name__ == '__main__':
    i = 647
    primes = find_primes_less_than(500000)
    factors = {}
    while True:
        if i in factors:
            f1 = factors[i]
        else:
            f1 = factors[i] = find_prime_factors(i, primes)
        while len(f1) != 4:
            i += 1
            if i in factors:
                f1 = factors[i]
            else:
                f1 = factors[i] = find_prime_factors(i, primes)
        if i+1 in factors:
            f2 = factors[i+1]
        else:
            f2 = factors[i+1] = find_prime_factors(i+1, primes)
        if len(f2) != 4:
            i += 1
        else:
            unionSet = f1.union(f2)
            interSet = f1.intersection(f2)
            if len(unionSet) == 8 and len(interSet) == 0:
                if i+2 in factors:
                    f3 = factors[i+2]
                else:
                    f3 = factors[i+2] = find_prime_factors(i+2, primes)
                if len(f3) != 4:
                    i += 2
                else:
                    unionSet = unionSet.union(f3)
                    interSet = interSet.intersection(f3)
                    if len(unionSet) == 12 and len(interSet) == 0:
                        if i+3 in factors:
                            f4 = factors[i+3]
                        else:
                            f4 = factors[i+3] = find_prime_factors(i+3, primes)
                        if len(f4) != 4:
                            i += 3
                        else:
                            unionSet = unionSet.union(f4)
                            interSet = interSet.intersection(f4)
                            if len(unionSet) == 16 and len(interSet) == 0:
                                print("The result is:", i)
                                exit(0)
        i += 1
