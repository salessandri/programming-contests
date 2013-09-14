#!/usr/bin/env python3

########################################################################
#   Solves problem 60 from projectEuler.net.
#   Finds the first set of 5 primes that concatenating any 2 of them
#   forms a prime.
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
#   You can contact me at san.lt.ss@gmail.com or salessandri@nasel.com
#   Visit my wiki at http://san-ss.wikidot.com
########################################################################

from CommonFunctions import find_primes_less_than, is_prime

primes = set()
non_primes = set()

def determine_prime(n):
    if n in primes:
        return True
    if n in non_primes:
        return False
    if is_prime(n):
        primes.add(n)
        return True
    else:
        non_primes.add(n)
        return False

if __name__ == '__main__':
    list_of_sets = []
    maxim = 0
    for prime in find_primes_less_than(10000)[1:]:
        for i in range(len(list_of_sets)):
            s = list_of_sets[i]
            enter = True
            str_prime = str(prime)
            for n in s:
                str_n = str(n)
                if not determine_prime(int(str_n + str_prime)) or not determine_prime(int(str_prime + str_n)):
                    enter = False
                    break
            if enter:
                newset = s.copy()
                newset.add(prime)
                if len(newset) == 5:
                    print("The result is:", sum(newset))
                    exit(0)
                list_of_sets.append(newset)
        list_of_sets.append(set([prime]))
